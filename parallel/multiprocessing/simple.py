from multiprocessing import Process
from time import sleep

def work(idx):
    sleep(1)
    print(f"worker {idx}")


processes = []
for i in range(10):
    processes.append(Process(target = work, args=(i,)))
    processes[-1].start()

for p in processes:
    p.join()



