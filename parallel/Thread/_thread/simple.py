#!/usr/bin/python3

import _thread
import time

def handler(tid, msg):
    print ("%d: %s" % (tid, msg))

_thread.start_new_thread(handler, (1, 'thread1',))
_thread.start_new_thread(handler, (2, 'thread2',))

time.sleep(1)
    
