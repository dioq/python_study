#!/usr/bin/python3
# -*- coding: utf-8 -*-

def init_dict():
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

    print("tinydict['Name']: ", dict['Name'])
    print("tinydict['Age']: ", dict['Age'])

    dict["AA"] = "aa"
    print(dict)


def traverse_dict():
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    print(dict)
    for key in dict:
        print(key)


def key_exist():
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    exist = dict.__contains__("name")
    if exist:
        print("key:name 存在")
    else:
        print("key:name 不存在")

    exist = dict.__contains__("Age")
    if exist:
        print("key:Age 存在")
    else:
        print("key:Age 不存在")


if __name__ == '__main__':
    # init_dict()
    # traverse_dict()
    key_exist()
