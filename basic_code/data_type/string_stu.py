#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# string 截取
def str_substr():
    str_test = "abcdefghijk0987654321"
    tmp = str_test[:3]  # 截取前 3 个字符
    print(tmp)

    tmp = str_test[3:]  # 截取第 3个字符 以后数据
    print(tmp)

    tmp = str_test[2:4]  # 截取 (2,4] 字符串
    print(tmp)


# string 拼接
def str_join():
    str1 = "abcde"
    str2 = "1234"
    str3 = str1 + str2  # 字符串拼接
    print(str3)


# string转bytes
def str_2_bytes():
    test_str = "abcdef"
    # 字符串转成 byte数组
    test_bytes = bytes(test_str, encoding="utf8")
    for item in test_bytes:
        print(item)


# bytes转string
def bytes_2_str():
    test_str = "abcdef"
    test_bytes = bytes(test_str, encoding="utf8")
    # byte数组 转字符串
    new_test_str = str(test_bytes, encoding='utf-8')
    print(new_test_str)


if __name__ == '__main__':
    # str_substr()
    # str_join()
    # str_2_bytes()
    bytes_2_str()
