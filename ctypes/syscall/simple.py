import ctypes, sys

raw_syscall = ctypes.CDLL(None).syscall
raw_syscall.restype = ctypes.c_long
raw_syscall.argtypes = ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long

# Make syscall
sysno = int(sys.argv[1])
ret = raw_syscall(sysno, 0, 0, 0, 0)
print('Syscall %d ret %s' % (sysno, repr(ret)))
