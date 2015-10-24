from elasticache_pyclient import MemcacheClient


class Connection_cache():

    mc = MemcacheClient('smarttoolsv2.1giena.cfg.usw2.cache.amazonaws.com:11211')

    def set_cache(self,key_cache,value):
        self.mc.set(key_cache,value)

    def get_cache(self,key_cache):
        self.mc.get(key_cache)
