class myObj:
    def __init__(self):
        self.index = 0
        self.max_num = 10

    def __getitem__(self, key):
        if isinstance(key, slice):
            return [ x for x in range(*key.indices(self.len()))]
        return key

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

