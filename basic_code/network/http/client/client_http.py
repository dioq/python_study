#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import requests
import json


# 测试 get 请求
def get_request(url):
    headers = {
        "User-Agent": "iOS",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "Connection": "keep-alive",
    }
    new_url = url + "?name=JOJO"
    response = requests.get(url=new_url, headers=headers)
    if response.status_code == 200:
        print("请求成功!")
        print(response.text)
    else:
        print(response.status_code)
        print("请求失败!")


# 测试 post 请求 参数为 json
def post_request(url):
    headers = {
        "User-Agent": "iOS",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Connection": "keep-alive",
    }

    param_dict = {"name": "JOJO", "age": 25}
    json_str = json.dumps(param_dict)
    data_bytes = bytes(json_str, encoding="utf8")
    response = requests.post(
        url=url, data=data_bytes, headers=headers, verify=False
    )  # 不验证 服务器 ssl 证书

    if response.status_code == 200:
        print("请求成功!")
        print(response.text)
    else:
        print(response.status_code)
        print("请求失败!")


# 提交 form 表单(可以实现文件上传)
def submit(url):
    # TEXT
    param = {"name": "JOJO", "age": 25, "address": "Beijing"}

    # FILE
    filename = "test.png"
    file_path = "./files/" + filename
    fd = open(file_path, "rb")

    files = {"file": fd}

    response = requests.post(
        url=url, data=param, files=files, verify=False
    )  # 不验证 服务器 ssl 证书
    if response.status_code == 200:
        print("请求成功!")
        print(response.text)
    else:
        print(response.status_code)
        print("请求失败!")

    fd.close()


# 文件下载
def download(url):
    response = requests.get(url=url)
    if response.status_code == 200:
        filename = "test.png"
        file_path = "./files/" + filename
        fd = open(file_path, "wb")
        fd.write(response.content)
        fd.close()
    else:
        print(response.status_code)
        print("请求失败!")


if __name__ == "__main__":
    test_get_url = "http://127.0.0.1:9000/get"
    test_post_json_url = "http://127.0.0.1:9000/post"
    test_download_url = "http://127.0.0.1:9000/download/test.png"
    test_formdata_url = "http://127.0.0.1:9000/form"
    # get_request(test_get_url)
    # post_request(test_post_json_url)
    # submit(test_formdata_url)
    # download(test_download_url)
