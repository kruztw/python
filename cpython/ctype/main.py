from ctypes import *


m = cdll.LoadLibrary('./simple.so')

print(m.add(c_int(1), c_int(2)))
