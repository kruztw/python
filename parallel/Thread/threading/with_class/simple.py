#!/usr/bin/python3

import threading

class myThread (threading.Thread):
    def __init__(self, tid, counter):
        threading.Thread.__init__(self)
        self.tid = tid
        self.counter = counter

    def run(self):
        threadLock.acquire()
        print_tid(self.tid, self.counter)
        threadLock.release()

def print_tid(tid,counter):
    for _ in range(counter):
        print (tid)


threadLock = threading.Lock()
thread1 = myThread(1, 5)
thread2 = myThread(2, 5)

thread1.start()         # start() 會調用 run()
thread2.start()
thread1.join()
thread2.join()
