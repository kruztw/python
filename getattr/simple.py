class A:
    bar = 1


a = A()
print(getattr(a, 'bar'))
