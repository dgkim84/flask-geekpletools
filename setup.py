from setuptools import setup

setup(
    name='flask-geekpletools',
    version='0.1.0',
    url='http://geekple.com/',
    license='',
    author='Daegeun Kim',
    author_email='dgkim84@gmail.com',
    maintainer='Daegeun Kim',
    maintainer_email='dgkim84@gmail.com',
    description='GeekPLE Tools for Flask',
    long_description='',
    platforms='any',
    zip_safe=False,
    packages=[
        'flask_geekpletools'
        , 'geekple'
        , 'geekple.tools'
        , 'geekple.tools.database'
    ],
    install_requires=[
        'Flask>=0.9'
        , 'thrift>=0.9.1'
        , 'zope.interface>=4.1.0'
        , 'twisted>=13.2.0'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)