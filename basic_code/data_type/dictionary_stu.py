#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def init_dict():
    dict_test = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

    print("tinydict['Name']: ", dict_test['Name'])
    print("tinydict['Age']: ", dict_test['Age'])

    dict_test["AA"] = "aa"
    print(dict_test)


def traverse_dict():
    dict_test = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    print(dict_test)
    for key in dict_test:
        print(key)


def key_exist():
    dict_test = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    exist = dict_test.__contains__("name")
    if exist:
        print("key:name 存在")
    else:
        print("key:name 不存在")

    exist = dict_test.__contains__("Age")
    if exist:
        print("key:Age 存在")
    else:
        print("key:Age 不存在")


if __name__ == '__main__':
    init_dict()
    traverse_dict()
    key_exist()
