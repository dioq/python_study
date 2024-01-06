#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import re


def test01():
    line = "this hdr-biz 123 model server 456"
    pattern = "123"
    # re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
    matchObj = re.match(pattern, line)
    print(matchObj)
    print(matchObj.group())
    print(matchObj.start())
    print(matchObj.end())
    print(matchObj.span())


def test02():
    line = "this hdr-biz 123 model server 456"
    pattern = "123"
    # re.search 扫描整个字符串并返回第一个成功的匹配
    matchObj = re.search(pattern, line)
    print(matchObj)
    print(matchObj.group())
    print(matchObj.start())
    print(matchObj.end())
    print(matchObj.span())


# 正则表达式 re.compile()
def test04():
    text = "the number is 20.50"
    r = re.compile(r"""
                    \d+ # 小数点前面的数字
                    \.? # 小数点
                    \d* # 小数点后面的数字
                    """, re.VERBOSE)
    ret = re.search(r, text)
    print(ret.group())


def test05():
    text = "the number is 20.50"
    r = re.compile(r"is", re.VERBOSE)
    matchObj = re.search(r, text)
    print(matchObj.group())
    print(matchObj.start())
    print(matchObj.end())
    print(matchObj.span())


if __name__ == '__main__':
    test05()
    # test04()
    # test02()
    # test01()
