# https://www.runoob.com/python3/python3-iterator-generator.html

#!/usr/bin/python3
 
import sys
 
def foo(n):                      # 生成器函数
    for i in range(n):
        yield i                  # 透過 yield 將狀態保存起來, 之後可用 next 迭代訪問

f = foo(10)                      # f 是一个迭代器，由生成器返回生成
 
print(type(f), f)
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
