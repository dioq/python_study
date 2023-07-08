#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 以16进制打印 list
def list_to_hex_string(list_data):
    list_str = '['
    for i in range(0, len(list_data)):
        list_str += '0x{:02X}'.format(list_data[i])
        if i < (len(list_data) - 1):
            list_str += ","
    list_str += ']'
    return list_str


# list 尾部追加
def list_append():
    # 定义一个list
    l1 = []
    for i in range(0, 10):
        # 在尾部追加
        l1.append(i * 10)
    l1_str = list_to_hex_string(l1)
    print(l1_str)

    l2 = [0x61, 0x62, 0x63, 0x64, 0x65, 0x66]
    # 2个list合并
    l3 = l1 + l2
    print(list_to_hex_string(l3))


# bytes 转 list
def bytes_2_list():
    test_str = "abcdef"
    test_bytes = bytes(test_str, encoding="utf8")
    l1 = list(test_bytes)
    print(list_to_hex_string(l1))


# list 转 bytes
def list_2_bytes():
    lt = [0x61, 0x62, 0x63, 0x64, 0x65, 0x66]
    my_bytes = bytes(lt)
    print(my_bytes)


if __name__ == '__main__':
    list_append()
    # bytes_2_list()
    # list_2_bytes()
