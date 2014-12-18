#-*- coding: utf-8 -*-
from threading import Thread
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
    thread0 = Thread(target=loop0)
    thread0.start()
    thread1 = Thread(target=loop1)
    thread1.start()

    thread0.join()
    thread1.join()
    print("Process done at ", time.ctime())

if "__main__" == __name__:
    main()
