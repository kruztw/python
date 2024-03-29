#!/usr/bin/env python3
import os
import struct
import types
from unicorn import *
from unicorn.x86_const import *

from syscall import hook_syscall


CODE = 0xdeadbeef000
STACK = 0xbabecafe000
MAIN = b'\x48\x83\xec\x20\x66\xc7\x44\x24\x0e\x00\x00\x48\x8d\x5c\x24\x0e\x48\xc7\x44\x24\x10\x00\x00\x00\x00\x48\xc7\x44\x24\x18\x00\x00\x00\x00\xb9\x44\x00\x00\x00\x48\x8d\x15\x8b\x01\x00\x00\xbe\x01\x00\x00\x00\x31\xc0\xbf\x01\x00\x00\x00\xe8\xbe\x01\x00\x00\xb9\x02\x00\x00\x00\x48\x89\xda\x31\xf6\x31\xff\x31\xc0\xe8\xab\x01\x00\x00\x8a\x44\x24\x0e\x3c\x32\x74\x39\x3c\x33\x74\x62\x3c\x31\x0f\x85\x04\x01\x00\x00\xb9\x12\x00\x00\x00\x48\x8d\x15\x35\x01\x00\x00\xbe\x01\x00\x00\x00\x31\xc0\xbf\x01\x00\x00\x00\xe8\x7a\x01\x00\x00\x48\x83\xc4\x20\x48\xbf\x00\xe0\xaf\xec\xab\x0b\x00\x00\xff\x27\xb9\x12\x00\x00\x00\x48\x8d\x15\xf6\x00\x00\x00\xbe\x01\x00\x00\x00\x31\xc0\xbf\x01\x00\x00\x00\xe8\x4d\x01\x00\x00\x48\x83\xc4\x20\x48\xbf\x00\xe0\xaf\xec\xab\x0b\x00\x00\xff\x27\xb9\x07\x00\x00\x00\x48\x8d\x15\xc2\x00\x00\x00\xbe\x01\x00\x00\x00\x31\xc0\xbf\x01\x00\x00\x00\xe8\x20\x01\x00\x00\x31\xf6\x31\xff\x48\x8d\x54\x24\x10\xb9\x08\x00\x00\x00\x31\xc0\xe8\x0b\x01\x00\x00\xb9\x07\x00\x00\x00\xbe\x01\x00\x00\x00\x31\xc0\x48\x8d\x15\x82\x00\x00\x00\xbf\x01\x00\x00\x00\xe8\xee\x00\x00\x00\x31\xf6\x31\xff\x31\xc0\x48\x8d\x54\x24\x18\xb9\x08\x00\x00\x00\xe8\xd9\x00\x00\x00\x48\x81\x7c\x24\x18\xff\x00\x00\x00\x0f\x87\xef\xfe\xff\xff\xb9\x07\x00\x00\x00\x48\x8d\x15\x41\x00\x00\x00\xbe\x01\x00\x00\x00\x31\xc0\xbf\x01\x00\x00\x00\xe8\xad\x00\x00\x00\x48\x8b\x4c\x24\x18\x31\xf6\x31\xff\x48\x8b\x54\x24\x10\x31\xc0\xe8\x98\x00\x00\x00\xe9\xb8\xfe\xff\xff\xbe\xff\x00\x00\x00\xbf\x3c\x00\x00\x00\x31\xc0\xe8\x82\x00\x00\x00\xe9\xa2\xfe\xff\xff\x64\x61\x74\x61\x3a\x20\x00\x73\x69\x7a\x65\x3a\x20\x00\x61\x64\x64\x72\x3a\x20\x00\x50\x61\x74\x68\x65\x74\x69\x63\x20\x68\x75\x6d\x61\x6e\x20\x3e\x0a\x00\x50\x6f\x77\x65\x72\x66\x75\x6c\x20\x61\x64\x6d\x69\x6e\x20\x3e\x0a\x00\x57\x65\x6c\x63\x6f\x6d\x65\x20\x74\x6f\x20\x75\x63\x5f\x6d\x61\x73\x74\x65\x65\x65\x72\x0a\x31\x2e\x20\x61\x64\x6d\x69\x6e\x20\x74\x65\x73\x74\x0a\x32\x2e\x20\x75\x73\x65\x72\x20\x74\x65\x73\x74\x0a\x33\x2e\x20\x70\x61\x74\x63\x68\x20\x64\x61\x74\x61\x0a\x3f\x3a\x20\x00\x48\x89\xf8\x48\x89\xf7\x48\x89\xd6\x48\x89\xca\x4d\x89\xc2\x4d\x89\xc8\x4c\x8b\x4c\x24\x08\x0f\x05\xc3'
TAIL = b'\x31\xc0\xb9\x32\x00\x00\x00\x48\x8d\x15\x55\x00\x00\x00\xbe\x01\x00\x00\x00\xbf\x01\x00\x00\x00\x48\x83\xec\x18\x66\x89\x44\x24\x0e\x31\xc0\xe8\x6d\x00\x00\x00\x31\xf6\x31\xff\x31\xc0\x48\x8d\x54\x24\x0e\xb9\x02\x00\x00\x00\xe8\x58\x00\x00\x00\x80\x7c\x24\x0e\x79\x75\x11\x48\x83\xc4\x18\x48\xbf\x00\xe0\xaf\xec\xab\x0b\x00\x00\xff\x67\x10\x31\xf6\xbf\x3c\x00\x00\x00\x31\xc0\xe8\x32\x00\x00\x00\x43\x6f\x6e\x67\x72\x61\x74\x75\x6c\x61\x74\x69\x6f\x6e\x73\x21\x20\x54\x65\x73\x74\x20\x73\x75\x63\x63\x65\x65\x64\x21\x0a\x54\x72\x79\x20\x61\x67\x61\x69\x6e\x3f\x20\x28\x79\x2f\x5b\x6e\x5d\x29\x00\x48\x89\xf8\x48\x89\xf7\x48\x89\xd6\x48\x89\xca\x4d\x89\xc2\x4d\x89\xc8\x4c\x8b\x4c\x24\x08\x0f\x05\xc3'

admin_offset = CODE + 0x6b - 5
writable = []
is_admin = False
uc = 0

def specific_memory_hook(uc, address, size, user_data):
    print("access specific address : ", hex(address))
    


def hook_mem_access(uc, access, address, size, value, user_data):
    print(f"access memory : {hex(address)} (rsp)")


def _safe_mem_write(self, address, data):
    print(f"write memory {hex(address)} : {data}")
    end = address + len(data)
    for page in writable:
        if address >= page and end <= page + 0x1000:
            self.mem_write(address, data)
            break
    else:
        raise UcError(UC_ERR_WRITE_PROT)


def p64(n):
    return struct.pack('<Q', n)


def init(uc):
    global writable

    uc.safe_mem_write = types.MethodType(_safe_mem_write, uc)

    uc.mem_map(CODE, 0x1000, UC_PROT_READ | UC_PROT_EXEC)
    uc.mem_write(CODE, b'\x90' * 0x1000)
    uc.mem_map(CODE + 0x1000, 0x1000, UC_PROT_ALL)
    uc.mem_write(CODE + 0x1000, b'\x90' * 0x1000)
    uc.mem_map(CODE + 0x2000, 0x1000, UC_PROT_READ | UC_PROT_EXEC)
    uc.mem_write(CODE + 0x2000, b'\x90' * 0x1000)
    uc.mem_write(CODE, MAIN)
    uc.mem_write(CODE + 0x2000, TAIL)

    uc.mem_map(STACK, 0x1000, UC_PROT_READ | UC_PROT_WRITE)
    uc.reg_write(UC_X86_REG_RSP, STACK + 0xf00)
    uc.mem_write(STACK, p64(CODE + 0x1000) + p64(CODE + 0x2000) + p64(CODE))

    writable = (CODE + 0x1000, STACK)

    uc.hook_add(UC_HOOK_INSN, hook_syscall, None, 1, 0, UC_X86_INS_SYSCALL)
    uc.hook_add(UC_HOOK_CODE, specific_memory_hook, None, CODE, CODE + 1)
    uc.hook_add(UC_HOOK_MEM_WRITE, hook_mem_access)


def main():
    global uc
    uc = Uc(UC_ARCH_X86, UC_MODE_64)
    init(uc)

    try:
        # 從 CODE 執行到 CODE + 0x3000
        uc.emu_start(CODE, CODE + 0x3000 - 1)
    except UcError as e:
        print("error...")


if __name__ == '__main__':
    main()

