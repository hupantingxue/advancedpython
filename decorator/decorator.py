#!/usr/bin/python2.6
#-*- coding:utf-8 -*-

import time

def log(func):
    '''Decorator'''
    def wrapper(*args, **kw):
        print "call %s" % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def now():
    "The function which to be decorated"
    print time.strftime("%Y%m%d %H:%M:%S" ,time.localtime())

if "__main__" == __name__:
    now()
