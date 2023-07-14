#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json

"""
json.dumps(): 对数据进行编码           Python Object       --->        JSON string
json.loads(): 对数据进行解码           JSON string         --->        Python Object
"""


# json 编码
def json_encode():
    data_dict = {
        'no': 1,
        'name': 'Runoob',
        'url': 'https://jobs8.cn'
    }
    print(data_dict)

    json_str = json.dumps(data_dict)
    print(type(json_str))
    print("JSON string:\n", json_str)


# json 解码,将 JSON string 转换为 Python 字典
def json_decode():
    json_str = "{\"no\": 1, \"name\": \"Runoob\", \"url\": \"https://jobs8.cn\"}"
    json_dict = json.loads(json_str)
    print(type(json_dict))
    print("json['name']: ", json_dict['name'])
    print("json['url']: ", json_dict['url'])


if __name__ == '__main__':
    json_encode()
    json_decode()
