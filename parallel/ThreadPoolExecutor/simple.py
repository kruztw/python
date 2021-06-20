from concurrent.futures import ThreadPoolExecutor, as_completed

def handler(arg):
    for i in range(100000):
        pass
    return f'Arg = {arg}'

args = ['a', 'b', 'c', 'd', 'e']

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = []
    for arg in args:
        future = executor.submit(handler, arg)
        futures.append(future)
    
    for future in as_completed(futures):
         print(future.result())

    results = executor.map(handler, args)
    for r in results:
        print(r)
