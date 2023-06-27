# -*- coding: utf-8 -*-

def test01():
    str_test = "0987654321abcdefghijk"
    tmp = str_test[:3]  # 截取前 3 个字符
    print(tmp)

    tmp = str_test[3:]  # 截取第 3个字符 以后数据
    print(tmp)

    tmp = str_test[2:4] # 截取 (2,4] 字符串
    print(tmp)


def test02():
    str1 = "abcde"
    str2 = "1234"
    str3 = str1 + str2  # 字符串拼接
    print(str3)


if __name__ == '__main__':
    test01()
    # test02()
