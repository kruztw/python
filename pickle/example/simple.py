import pickle
import os

class Foo:
    attr = 'A class attribute'

class A:
    def __reduce__(self):
        return(os.system, (('ls'),))

foo = pickle.dumps(Foo)
print(pickle.loads(foo))


a = pickle.dumps(os.system('ls'))
#print(pickle.loads(a))

pickle.loads(b"cos\nsystem\n(S'echo hello'\ntR.")
