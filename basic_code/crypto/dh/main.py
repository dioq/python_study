#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ctypes

dll = ctypes.cdll.LoadLibrary
lib = dll('./libdh.so')  # 刚刚生成的库文件的路径

alice_private_key = 0x50db7349  # Alice的私钥
alice_public_key = lib.perform_dh_key_exchange(alice_private_key, 16807)
print(alice_public_key)

bob_public_key = 0x35a93998

common_key = lib.mod_exp(bob_public_key, alice_private_key, 2147483647)
print("common_key:", common_key)
