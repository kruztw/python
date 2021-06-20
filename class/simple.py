#!/usr/bin/python

 
class A(object):
    def __init__(self, arg1):
        self.arg = arg1

    def func1(self):  
        print ('call func1', self)

    @classmethod                # 允許用 class 直接呼叫, 不用實例化 ( obj = A(1), obj.func2(1)), 第一個參數為 class
    def func2(cls, bar):
        print ('call func2', type(cls), cls)
        cls(1).func1()          # OK
        return cls(bar)         # 可以 return obj 回去, 當然也可以 return 其他東西

    @staticmethod
    def func3(bar):                # 與 classmethod 差別在沒有 class 作為第一個參數
        print ('call func3', bar)
 

A.func2(1)               # OK
B = A.func2(2)           # OK
B.func1()                # OK
#A.func1()               # No
A_obj = A(3)
A_obj.func1()

A.func3(4)
