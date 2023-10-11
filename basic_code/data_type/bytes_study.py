#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 二进制数据以16进制打印
def show_binary_by_hex(data):
    lt: list = list(data)
    for i in range(0, len(lt)):
        item = '{:02X} '.format(lt[i])
        print(item, end="")
        if (i + 1) % 0x10 == 0:
            print("")


def string_to_bytes():
    test_str = "This is just a test string."
    # 字符串 以utf8 码表 解码成 bytes
    test_bytes = bytes(test_str, encoding="utf8")
    show_binary_by_hex(test_bytes)


def hexstring_to_bytes():
    test_str = "54686973206973206A7573742061207465737420737472696E672E"
    # hex string 转 bytes
    test_bytes = bytes.fromhex(test_str)
    show_binary_by_hex(test_bytes)


if __name__ == '__main__':
    # string_to_bytes()
    hexstring_to_bytes()
