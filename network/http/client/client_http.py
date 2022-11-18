#!/usr/bin/python3

import json

import requests

http_get_url = "http://127.0.0.1:8090/get"
http_post_url = "http://127.0.0.1:8090/post"
http_post_formdata_url = "http://127.0.0.1:8090/postform"


# 测试 get 请求
def getFunc():
    headers = {
        "User-Agent": "iOS",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "Connection": "keep-alive"
    }
    response = requests.get(url=http_get_url, headers=headers)
    if response.status_code == 200:
        print("请求成功!")
        print(response.text)
    else:
        print(response.status_code)
        print("请求失败!")


# 测试 post 请求 参数为 json
def postFunc():
    param = {"name": "JOJO", "age": 25}
    # print(param)
    headers = {
        "User-Agent": "iOS",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Connection": "keep-alive"
    }
    response = requests.post(url=http_post_url, json=param, headers=headers, verify=False)  # 不验证 服务器 ssl 证书

    # 或者
    # data = json.dumps(param)
    # response = requests.post(url=http_post_url, data=data, headers=headers, verify=False)  # 不验证 服务器 ssl 证书

    if response.status_code == 200:
        print("请求成功!")
        print(response.text)
    else:
        print(response.status_code)
        print("请求失败!")


# 测试 post 请求 参数为 formdata
def postFormdataFunc():
    headers = {
        "User-Agent": "iOS",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        "Connection": "keep-alive"
    }
    params = "name=JOJO&age=25"
    # print(params)
    response = requests.post(url=http_post_formdata_url, params=params, headers=headers)
    if response.status_code == 200:
        print("请求成功!")
        print(response.text)
    else:
        print(response.status_code)
        print("请求失败!")


if __name__ == "__main__":
    getFunc()
    postFunc()
    postFormdataFunc()
