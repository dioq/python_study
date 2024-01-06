#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

"""
os.system(cmd)
参数说明:
cmd：要执行的命令。
功能:
os.system()是在当前进程中打开一个子shell（子进程）来执行系统命令. 无法处理返回值

os.popen(cmd, mode='r', buffering=-1)
参数说明:
cmd：要执行的命令。
mode：打开文件的模式，默认为'r'，用法与open()相同。
buffering：0意味着无缓冲；1意味着行缓冲；其它正值表示使用参数大小的缓冲。负的bufsize意味着使用系统的默认值，一般来说，对于tty设备，它是行缓冲；对于其它文件，它是全缓冲。
功能:
这个方法会打开一个管道，返回结果是一个连接管道的文件对象，该文件对象的操作方法同open()，可以从该文件对象中读取返回结果。如果执行成功，不会返回状态码，如果执行失败，则会将错误信息输出到stdout，并返回一个空字符串。
"""


def way01Func():
    cmd = 'ls'
    # 无法获得cmd命令的输出
    os.system(cmd)


def way02Func():
    cmd = 'ls'
    res = os.popen(cmd)
    output_str = res.read()  # 获得输出字符串
    print(output_str)


def way03Func():
    cmd = "cat ./target.txt"
    res = os.popen(cmd)
    output_str = res.read()  # 获得输出字符串
    print("target 内容:")
    print(output_str)


def way04Func():
    uuid = "8ca333c7df73fd84c9b5c1fc2ec914875c6ff976"
    cmd = "ideviceinstaller -u {uid} -l".format(uid=uuid)  # 这行命令是在mac 上读取 所连接的手机上所有安装的app 信息
    print(cmd)
    file = os.popen(cmd)
    lines = file.readlines()  # 获得输出字符串
    for line in lines:
        if line is not None and line != "":
            print(line)


if __name__ == "__main__":
    # way01Func()
    # way02Func()
    # way03Func()
    way04Func()
