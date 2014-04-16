from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift.transport import THttpClient
from thrift.protocol import TBinaryProtocol

from geekple.tools.database import Queries
from geekple.tools.database.ttypes import *

import socket

framed = True

class GPTools:
    def __init__(self, hostname='127.0.0.1', port=8195):
        socket = TSocket.TSocket(hostname, port)
        if framed:
            transport = TTransport.TFramedTransport(socket)
        else:
            transport = TTransport.TBufferedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        self.client = Queries.Client(protocol)
        try:
            transport.open()
        except TTransport.TTransportException as e:
            pass

        self.transport = transport

    def put(self, path, queries):
        try:
            self.client.put(
                path
                , [Query('', statement, map(str, parameters), int(stime*1000), int(etime*1000)) for statement, parameters, stime, etime in queries]
            )
        except TTransport.TTransportException as e:
            pass
        except socket.error as e:
            pass

