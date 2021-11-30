from types import FunctionType

def foo():
    print("hello world")

FunctionType(foo.__code__, foo.__globals__, foo.__defaults__, foo.__closure__)()
