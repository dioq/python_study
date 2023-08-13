#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from unicorn import *
from unicorn.arm64_const import *

# Machine Config
ADDRESS = 0x10000  # 开始执行的地址
MEMORY = 2 * 1024 * 1024  # 内存
STACK = 0x80000000 + 0x10000 * 6  # 栈

# code to be emulated
'''
add x0, x1, x2
sub x0, x0, x3
'''
ARM_CODE = b"\x20\x00\x02\x8B\x00\x00\x03\xCB"


# callback for tracing basic blocks
def hook_block(uc, address, size, user_data):
    print(">>> Tracing basic block at 0x%x, block size = 0x%x" % (address, size))


# callback for tracing instructions
def hook_code(uc, address, size, user_data):
    print(">>> Tracing instruction at 0x%x, instruction size = 0x%x" % (address, size))


# Test ARM
def test_aarch64():
    print("Emulate AArch64 code")
    try:
        # Initialize emulator in AArch64 mode
        mu = Uc(UC_ARCH_ARM64, UC_MODE_ARM)
        # map 2MB memory for this emulation
        mu.mem_map(ADDRESS, MEMORY)
        # write machine code to be emulated to memory
        mu.mem_write(ADDRESS, ARM_CODE)

        # initialize machine registers
        mu.reg_write(UC_ARM64_REG_X1, 0x10)
        mu.reg_write(UC_ARM64_REG_X2, 0x50)
        mu.reg_write(UC_ARM64_REG_X3, 0x40)
        mu.reg_write(UC_ARM64_REG_SP, STACK)

        # tracing all basic blocks with customized callback
        mu.hook_add(UC_HOOK_BLOCK, hook_block)

        # tracing one instruction at ADDRESS with customized callback
        mu.hook_add(UC_HOOK_CODE, hook_code, begin=ADDRESS, end=ADDRESS)

        # emulate machine code in infinite time
        mu.emu_start(ADDRESS, ADDRESS + len(ARM_CODE))

        # now print out some registers
        print(">>> Emulation done. Below is the CPU context")

        x0 = mu.reg_read(UC_ARM64_REG_X0)
        x1 = mu.reg_read(UC_ARM64_REG_X1)
        x2 = mu.reg_read(UC_ARM64_REG_X2)
        x3 = mu.reg_read(UC_ARM64_REG_X3)
        print('x0 = 0x%lx' % x0)
        print('x1 = 0x%lx' % x1)
        print('x2 = 0x%lx' % x2)
        print('x3 = 0x%lx' % x3)

    except UcError as e:
        print("ERROR: %s" % e)


if __name__ == '__main__':
    test_aarch64();
    print("=" * 26)
