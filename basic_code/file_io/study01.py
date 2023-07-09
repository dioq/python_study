#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import shutil

"""
模式         描述
r			默认模式，打开文件进行读取
w			打开文件用于写入。如果文件不存在，它创建一个新文件。如果文件存在，它截断文件
x			创建一个新的文件。如果文件已经存在，则操作失败
a			以追加模式打开文件。如果文件不存在，则创建一个新文件
t			默认模式。它以文本模式打开
b			以二进制模式打开
+			打开一个文件进行读写(更新)
"""


# 写入 string 到文件中
def write_string():
    f = open("test.txt", "w")
    f.write("This is only a test.")
    f.close()


# 写入 binary data 到文件中
def write_binary():
    test_str = "abcdef"
    # 字符串转成 byte数组
    test_bytes = bytes(test_str, encoding="utf8")

    f = open("test2.txt", "wb")
    f.write(test_bytes)
    f.close()


def file_delete():
    path = "./test.txt"
    os.remove(path)
    os.remove("./test2.txt")


# 判断文件或目录是否存在
def judge():
    path = "./test2.txt"
    status = os.path.exists(path)  # 判断目标是否存在
    if status:
        print(path + " 存在")
    else:
        print(path + " 不存在")

    status = os.path.isdir(path)  # 判断目标是否目录
    if status:
        print(path + " 是目录")
    else:
        print(path + " 不是目录")

    status = os.path.isfile(path)  # 判断目标是否文件
    if status:
        print(path + " 是文件")
    else:
        print(path + " 不是文件")


def directory_create():
    # 创建单级目录
    path = "tmp"
    os.mkdir(path)

    # 创建多级目录
    path2 = "./tmp1/tmp2"
    os.makedirs(path2)


def directory_delete():
    path = "tmp"
    os.rmdir(path)  # 只能删除空目录
    shutil.rmtree("./tmp1")  # 空目录、有内容的目录都可以删


# 一次读取全部文件
def read_file1():
    f = open("test2.txt", "r")
    # read()            方法表示一次读取文件全部内容，该方法返回字符串。
    lines = f.read()
    print(lines)
    print(type(lines))
    f.close()


def read_file2():
    f = open("test2.txt", "r")
    # readline()        每次读出一行内容，读取时占用内存小，比较适合大文件，该方法返回一个字符串对象
    line = f.readline()
    while line:
        print(line)
        print(type(line))
        line = f.readline()
    f.close()


def read_file3():
    f = open("test2.txt", "r")
    # readlines()       读取整个文件所有行，保存在一个列表(list)变量中，每次读取一行，但读取大文件会比较占内存。
    lines = f.readlines()
    for line in lines:
        print(line)
        print(type(line))
    f.close()


if __name__ == "__main__":
    # read_file3()
    # read_file2()
    read_file1()
    # write_string()
    # write_binary()
    # file_delete()
    # directory_create()
    # directory_delete()
