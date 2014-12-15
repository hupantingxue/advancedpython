#-*- coding: utf-8 -*-
import thread
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
    print("Process start at ", time.ctime())
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    time.sleep(6)
    print("Process done at ", time.ctime())

if "__main__" == __name__:
    main()
