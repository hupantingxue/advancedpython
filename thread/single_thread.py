#-*- coding: utf-8 -*-
import time

def loop0():
    print("start loop0 at ", time.ctime())
    time.sleep(4)
    print("finish loop0 at ", time.ctime())

def loop1():
    print("start loop1 at ", time.ctime())
    time.sleep(2)
    print("finish loop1 at ", time.ctime())

def main():
    loop0()
    loop1()

if "__main__" == __name__:
    print("Process start at ", time.ctime())
    main()
    print("Process done at ", time.ctime())
