#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import base64


def list_to_hex_string(list_data):
    list_str = '['
    for i in range(0, len(list_data)):
        list_str += '0x{:02X}'.format(list_data[i])
        if i < (len(list_data) - 1):
            list_str += ","
    list_str += ']'
    return list_str


# base64 编码和解码
def test_base64():
    test_str = "abcdef098765421"
    # 字符串转成 byte数组
    test_bytes = bytes(test_str, encoding="utf8")
    print("origin bytes:\n", list_to_hex_string(list(test_bytes)))

    # base64 编码
    encode_test_bytes = base64.b64encode(test_bytes)
    print(type(encode_test_bytes))
    print("base64 encode:\n", list_to_hex_string(list(encode_test_bytes)))
    # 打印出来看一下
    new_test_str = str(encode_test_bytes, encoding='utf-8')
    print(new_test_str)

    # base64 解码
    decode_test_bytes = base64.b64decode(encode_test_bytes)
    print(type(decode_test_bytes))
    print("base64 decode:\n", list_to_hex_string(list(decode_test_bytes)))
    # 打印出来看一下
    new_test_str = str(decode_test_bytes, encoding='utf-8')
    print(new_test_str)


# hex 编码和解码
def test_hex():
    test_str = "1234567890abcdef"

    test_bytes = bytes(test_str, encoding='utf8')
    print(type(test_bytes))
    print(list_to_hex_string(list(test_bytes)))

    test_bytes2 = bytes.decode(test_bytes, encoding='utf8')
    print(type(test_bytes2))
    print(test_bytes2)


if __name__ == '__main__':
    test_base64()
    # test_hex()
