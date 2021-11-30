from types import CodeType, FunctionType

class custom(object):
    def __init__(self, arg):
        print(f'__init__: {arg}')

    def __call__(self, *args, **kwargs):
        print(f'__call__: {args} {kwargs}')

    def __str__(self):
        print(f'__str__: ')
        return ""

    def __truediv__(self, arg):
        print(f'__truediv__: {arg}')
        return self

    def __getattribute__(self, name):
        print(f'__getattribute__: {name}')
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            return self


class FakeGlobals(dict):
    def __init__(self, d):
        self.update(d)

    def __getitem__(self, key):
        if key not in self:
            if key in self['__builtins__'].__dict__:
                return self['__builtins__'].__dict__[key]
            return custom(key)
        return dict.__getitem__(self, key)


def foo():
    url = www.httpbin.org/anything/test/'[special-path]'/index.html
    return url(method='POST')

new_function = FunctionType(foo.__code__,
                           FakeGlobals(foo.__globals__),
                           foo.__name__, foo.__defaults__, foo.__closure__)

new_function()
