try:
    import cPickle as pickle
except ImportError:
    import pickle

import pytyrant
import time

from django.core.cache.backends.base import BaseCache
from django.utils.encoding import smart_unicode, smart_str

class CacheClass(BaseCache):
    def __init__(self, server, params):
        "Connect to Tokyo Tyrant, and set up cache backend."
        BaseCache.__init__(self, params)
        host, port = server.split(':')
        self._cache = pytyrant.Tyrant.open(host, int(port))
        
    def _prepare_key(self, raw_key):
        return smart_str(raw_key)
        
    def add(self, key, value, timeout=0):
        "Add a value to the cache. Returns ``True`` if the object was added, ``False`` if not."
        try:
            value = pickle.dumps(value)
            self._cache.putkeep(self._prepare_key(key), value)
        except pytyrant.TyrantError:
            return False
        return True

    def get(self, key, default=None):
        "Retrieve a value from the cache. Returns unpicked value if key is found, 'default' if not. "
        try:
            value = self._cache.get(self._prepare_key(key))
        except pytyrant.TyrantError:
            return default
        value = pickle.loads(value)
        if isinstance(value, basestring):
            return smart_unicode(value)
        else:
            return value
        
    def set(self, key, value, timeout=0):
        "Persist a value to the cache."
        value = pickle.dumps(value)
        self._cache.put(self._prepare_key(key), value)
        return True

    def delete(self, key):
        "Remove a key from the cache."
        self._cache.out(self._prepare_key(key))
        
    def get_many(self, keys):
        "Retrieve many keys."
        many = self._cache.mget(keys)
        return [{k:pickle.loads(v)} for k,v in many]

    def flush(self, all_dbs=False):
        self._cache.vanish()

    def incr(self, key, delta=1):
        "Atomically increment ``key`` by ``delta``."
        return self._cache.addint(self._prepare_key(key), delta)
        
# TODO it is crashed program
#    def close(self, **kwargs):
#        "Disconnect from the cache."
#        self._cache.close()

