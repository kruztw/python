# rq worker
# python3 app.py

import jobs

from time import sleep
from rq import Queue
import redis

def run():
    q = Queue(connection = redis.Redis())
    j = q.enqueue(jobs.count, 'hello world')
    sleep(1)
    print(j.result)

run()
