#-*- coding: utf-8 -*-
from threading import Thread
import time

def loop(idx, nsec):
    print("start loop", idx, " at ", time.ctime())
    time.sleep(nsec)
    print("start loop", idx, " at ", time.ctime())

def main():
    print("Process start at ", time.ctime())
    thread0 = Thread(target=loop, args=(0, 4))
    thread0.start()
    thread1 = Thread(target=loop, args=(1, 2))
    thread1.start()

    thread0.join()
    thread1.join()
    print("Process done at ", time.ctime())

if "__main__" == __name__:
    main()
