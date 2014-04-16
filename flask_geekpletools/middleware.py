from flask import _request_ctx_stack, request
from sqlalchemy.event import listen

from .client import GPTools

try:
	from flask import _app_ctx_stack
except:
	_app_ctx_stack = None

import time
import sys

if sys.platform == 'win32':
    _timer = time.clock
else:
    _timer = time.time

connection_stack = _app_ctx_stack or _request_ctx_stack

class GPToolsMiddleware:
    """
    """
    def __init__(self, app, engine, **options):
        self.wsgi_app = app.wsgi_app
        self.client = GPTools(**options)
        app.after_request(self.request_finished)
        listen(engine, 'after_cursor_execute', self.after_cursor_execute)
        listen(engine, 'before_cursor_execute', self.before_cursor_execute)

    def before_cursor_execute(self, conn, cursor, statement
            , parameters, context, executemany):
        if connection_stack.top is not None:
            setattr(context, '_start_time', _timer())

    def after_cursor_execute(self, conn, cursor, statement
            , parameters, context, executemany):
        top = connection_stack.top
        if top is not None:
            queries = getattr(top, '_tools_sqlalchemy_queries', None)
            if not queries:
                queries = []
                setattr(top, '_tools_sqlalchemy_queries', queries)
            queries.append((statement, parameters, getattr(context, '_start_time'), _timer()))

    def request_finished(self, response):
        queries = getattr(connection_stack.top, '_tools_sqlalchemy_queries', None)
        if queries:
            self.client.put(request.path, queries)
        return response

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)
