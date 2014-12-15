#-*- coding: utf-8 -*-
import thread
import time

def loop(nloop, nsec, lock):
    print("start loop", nloop," at ", time.ctime())
    time.sleep(nsec)
    print("finish loop", nloop," at ", time.ctime())
    lock.release()

def main():
    print("Process start at ", time.ctime())
    loops = [4, 2]
    nloops = len(loops)
    locks = []

    for ii in range(nloops):
        lock = thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for ii in range(nloops):
        thread.start_new_thread(loop, (nloops, loops[ii], locks[ii]))

    for lock_item in locks:
        while lock_item.locked():
            pass
    print("Process done at ", time.ctime())

if "__main__" == __name__:
    main()
