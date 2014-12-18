#-*- coding: utf-8 -*-
from threading import Thread
import time

class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        apply(self.func, self.args)

def loop(idx, nsec):
    print("start loop", idx, " at ", time.ctime())
    time.sleep(nsec)
    print("start loop", idx, " at ", time.ctime())

def main():
    loops = [4, 2]
    threads = []
    print("Process start at ", time.ctime())
    for ii in range(len(loops)):
        t = Thread(
                target=ThreadFunc(loop, (ii, loops[ii]), loop.__name__))
        threads.append(t)
 
    for t in threads:
        t.start()
 
    for t in threads:
        t.join()

    print("Process done at ", time.ctime())

if "__main__" == __name__:
    main()
