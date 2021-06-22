# https://docs.python.org/zh-cn/3/tutorial/errors.html

import sys

# ValueError

try:
    int('a')
except (ValueError, KeyboardInterrupt) as e:   # 可以用 () 指定多個 exception
    print("Error:", e)


# OSError
try:
    open("wtf")
except OSError as e:
    print("Error:", e)
    print("exc_info:", sys.exc_info()) 


# ZeroDivisionError
try:
    1/0
except ZeroDivisionError as e:
    print("Error:", e)


# 自行指定 Exception
class myException(Exception):
    pass

try:
    raise myException("myArg")
except myException as e:
    print("Error:", e.args[0])


# 帶參數
try:
    raise Exception("arg1", "arg2")
except Exception as e:
    print("type: ", type(e), e, e.args[0])


# try except else
try:
    print("try ", end='')
except:
    print("except ", end='')
else:
    print("else ")


# try [except] finally    => except 可省, 另外也可以是 try except else finally
try:
    print("try ", end='')
    1/0
except:
    print("except ", end='')
finally:
    print("finally ")






