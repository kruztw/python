def noarg_wrapper(func):              # func == noarg
    def wrapper():
        print("noarg_wrapper")
        return func()                 # exec noarg()
    return wrapper

@noarg_wrapper
def func1():
    print("noarg")


func1()

print('\n--------------------------------------\n')

def func_args_wrapper(func):
    def wrapper(args):
        print("wrapper: ", args)
        return func(args)
    return wrapper

@func_args_wrapper
def func2(args):
    print("func2 args: ", args)


func2("hello")


print('\n--------------------------------------\n')


def wrapper_with_args(wrapper_args):
    def func_args_wrapper(func):
        def wrapper(func_args):
            print("wrapper: ", func_args)
            return func(func_args)
        return wrapper

    print("wrapper_args: ", wrapper_args)
    return func_args_wrapper

@wrapper_with_args("wrapper_arg")
def func3(args):
    print("func3 args: ", args)


func3("hi")
