# -*- coding: utf-8 -*-


import time


class cache():
    def __init__(self,size:int,ttl:int):
        self.size=size
        self.ttl=ttl
        self.kv=dict()
        self.timed=dict()

    def set(self,key,val):
        if len(self.kv)<self.size:
            self.kv[key]=val
            self.timed[key]=time.time()
        else:
            dval=max(self.timed.values())
            for k,v in self.timed.items():
                if v == dval:
                    dkey=k
            del self.timed[dkey]
            del self.kv[dkey]
            self.kv[key]=val
            self.timed[key]=time.time()

    
    def get(self, key):
        if time.time()-self.timed[key]>=self.ttl:
            print("Time out Error! Cache memory location purged!")
            del self.timed[key]
            del self.kv[key]
        else:
            self.timed[key]=time.time()
            return self.kv[key]
            


c = cache(size=10, ttl=3)
c.set(key="a", val="1") # insert to cache
assert c.get(key="a") == "1" # read from cache
time.sleep(3)
c.get("a")
