#!/usr/bin/python2.6
#-*- coding:utf-8 -*-

import time
import functools

def log(text):
    def decorator(func):
        '''Decorator'''

        @functools.wraps(func)
        def wrapper(*args, **kw):
            '''wrapper'''

            print "begin call %s with %s" % (func.__name__, text)
            rv = func(*args, **kw)
            print "end call %s with %s" % (func.__name__, text)
            return rv
        return wrapper
    return decorator

@log('execute')
def now():
    "The function which to be decorated"
    print time.strftime("%Y%m%d %H:%M:%S" ,time.localtime())

if "__main__" == __name__:
    now()
