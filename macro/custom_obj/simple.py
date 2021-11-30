class myObj:
    def __init__(self):
        self.index = 0
        self.max_num = 10

    def __getitem__(self, key):
        if isinstance(key, slice):
            return [ x for x in range(*key.indices(self.len()))]
        return key

    def __truediv__(self, denomi):
        print("__truediv__: ", denomi)
        return self

    def __str__(self):
        print('__str__: ')
        return ""

    def __call__(self, *args, **kwargs):
        print("__call__: ", args, kwargs)
        return self    

    def __getattribute__(self, attr):
        try:
            return object.__getattribute__(self, attr)
        except AttributeError:
            return f"attr '{attr}' not found"

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < self.max_num:
            return self.index
        else:
            self.index = 0
            raise StopIteration

    def len(self):
        return self.max_num


obj = myObj()

print(obj[3])
print(obj[2:5])
for i in obj:
    print(i)



obj/1
str(obj)
obj(1, 2, key="val")
print(obj.fuck)
