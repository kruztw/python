class foo:
    def __init__(self):
        pass

    @property
    def private(self):
        print("get variable")
        return self._name

    @private.setter
    def private(self, val):
        print("set variable")
        self._name = val


f = foo()
f.private = 'b'  # call setter, if you comment setter, you can't change f.private
print(f.private) # call getter, if you comment getter, error "NameError: name 'private' is not defined" will pop up

f._name = 'c' 
print(f._name)   # c, now f.private is 'c' too
print(f.private) # c, call getter
