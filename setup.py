#!/usr/bin/env python

from distutils.core import setup

VERSION = '0.1'
DESCRIPTION = "Tokyo Tyrant cache backend for Django"
LONG_DESCRIPTION = """
Django cache backend using the Tokyo Tyrant to store cache. You also need to 
install 'pytyrant' (pure python client implementation of the binary Tokyo Tyrant
protocol).

Tokyo Tyrant is the de facto database server for Tokyo Cabinet written and
maintained by the same author. It supports a REST HTTP protocol, memcached,
and its own simple binary protocol.
"""

CLASSIFIERS = filter(None, map(str.strip,
"""                 
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python
Topic :: Database :: Front-Ends
Topic :: Software Development :: Libraries :: Python Modules
""".splitlines()))


setup(
    name="django-tyrant-cache",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    author="Anatoly Vostryakov",
    author_email="a.vostrjakov@gmail.com",
    url="http://github.com/avostryakov/django-tyrant-cache",
    license="MIT License",
    py_modules=['tyrant_cache'],
    platforms=['any'],
)
