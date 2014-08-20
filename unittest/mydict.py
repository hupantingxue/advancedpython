#!/usr/bin/env  python
#-*- coding: utf-8 -*-

class MyDict(dict):
    """
        pass
    """
    def __init__(self, **kw):
        super(MyDict, self).__init__(**kw)

    def __getatrr__(self, key):
        try:
            return self[key]
        except keyError:
            raise AttributeError(r"Dict object has no %s object" %(key))

    def __setattr__(self, key, value):
        self[key] = value

if "__main__" == __name__:
    d1 = MyDict(k1="v1", k2=2)
    print d1
