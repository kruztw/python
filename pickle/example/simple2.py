# https://docs.python.org/3/library/pickle.html

import builtins
import io
import pickle

safe_builtins = {
    'range',
    'complex',
    'set',
    'frozenset',
    'slice',
}

class RestrictedUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == "builtins" and name in safe_builtins:
            return getattr(builtins, name)
        raise pickle.UnpicklingError("global '%s.%s' is forbidden" % (module, name))

def restricted_loads(s):
    return RestrictedUnpickler(io.BytesIO(s)).load()


restricted_loads(b"cos\nsystem\n(S'echo hello world'\ntR.")
