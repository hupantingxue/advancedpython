#!/usr/bin/python2.6
#-*- coding:utf-8 -*-

import functools
import time

def log(func):
    '''Decorator'''

    @functools.wraps(func)
    def wrapper(*args, **kw):
        print "begin call %s" % func.__name__
        rv = func(*args, **kw)
        print "end call %s" % func.__name__
        return rv
    return wrapper

@log
def now():
    "The function which to be decorated"
    print time.strftime("%Y%m%d %H:%M:%S" ,time.localtime())
    return 'just return1', 'return 2'

if "__main__" == __name__:
    now()
