#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# hex string 打印二进制序列
def extra2_binary(data):
    b = bin(int(data, 16))[2:].zfill(8 * 4)
    print(b)


# 二进制数据以16进制打印
def show_binary_by_hex(data):
    lt = list(data)
    for i in range(0, len(lt)):
        item = '{:02X} '.format(lt[i])
        print(item, end="")
        if (i + 1) % 0x10 == 0:
            print("")


def test1():
    extra2_binary("D2C00212")


def test2():
    test_str = "abcdefoiqekljlkdanknzciaieqowejlqkejqadadkal"
    test_bytes = bytes(test_str, encoding="utf8")
    show_binary_by_hex(test_bytes)


if __name__ == '__main__':
    # test1()
    test2()
