#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ctypes

dll = ctypes.cdll.LoadLibrary
lib = dll('./test.so')  # 刚刚生成的库文件的路径
ret = lib.foo(1, 3)
print(ret)
