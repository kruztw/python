#!/usr/bin/python3

from threading import Thread, Lock

def handler(arg1, arg2):
    threadLock.acquire()
    print_tid(arg1, arg2)
    threadLock.release()

def print_tid(tid, counter):
    for _ in range(counter):
        print (tid)


threadLock = Lock()
thread1 = Thread(target=handler, args=(1, 5,))
thread2 = Thread(target=handler, args=(2, 5,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

