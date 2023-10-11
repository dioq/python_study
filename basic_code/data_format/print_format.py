#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def test1():
    name = "Dio"
    age = 20
    height = 180.0
    print(f"name={name},age={age},height={height}")


def test2():
    name = "Dio"
    age = 20
    height = 180.0
    print("name={name},age={age},height={height}".format(name=name, age=age, height=height))


def test3():
    # end="" 输出尾部结束符
    print("This is a test string.")
    print("This is a test string.", end="")
    print("This is a test string.", end=">")


if __name__ == '__main__':
    # test1()
    # test2()
    test3()
