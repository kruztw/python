# ref: https://www.geeksforgeeks.org/python-sys-settrace/

from sys import settrace

def my_tracer(frame, event, arg = None):
    code = frame.f_code
    func_name = code.co_name
    line_no = frame.f_lineno
  
    print(f"A {event} encountered in \
    {func_name}() at line number {line_no} ")
  
    return my_tracer
  
  
def fun():
    return "GFG"
  
def check():
    return fun()
  
settrace(my_tracer)
  
check()
