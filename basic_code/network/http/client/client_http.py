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
        "Connection": "keep-alive"
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
def post_json_request(url):
    headers = {
        "User-Agent": "iOS",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Connection": "keep-alive"
    }

    param_dict = {"name": "JOJO", "age": 25}
    json_str = json.dumps(param_dict)
    data_bytes = bytes(json_str, encoding="utf8")
    response = requests.post(url=url, data=data_bytes, headers=headers, verify=False)  # 不验证 服务器 ssl 证书

    if response.status_code == 200:
        print("请求成功!")
        print(response.text)
    else:
        print(response.status_code)
        print("请求失败!")


# 测试 post 请求 url 和 body 里都有参数
def post_form_request(url):
    headers = {
        "User-Agent": "iOS",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
        "Connection": "keep-alive"
    }

    param_form = "name=JOJO&age=25&name=Beijing"
    data_bytes = bytes(param_form, encoding="utf8")
    response = requests.post(url=url, data=data_bytes, headers=headers, verify=False)  # 不验证 服务器 ssl 证书
    if response.status_code == 200:
        print("请求成功!")
        print(response.text)
    else:
        print(response.status_code)
        print("请求失败!")


def upload_file(url):
    filename = "t1.png"
    file_path = "./files/" + filename
    fd = open(file_path, "rb")

    files = {"file": fd}

    response = requests.post(url, files=files)
    if response.status_code == 200:
        print("请求成功!")
        print(response.text)
    else:
        print(response.status_code)
        print("请求失败!")

    fd.close()


if __name__ == "__main__":
    test_get_url = "http://127.0.0.1:8090/get"
    test_post_json_url = "http://127.0.0.1:8090/post"
    test_post_form_url = "http://127.0.0.1:8090/postform"
    test_upload_url = "http://127.0.0.1:8090/upload"
    test_download_url = "http://127.0.0.1:8090/download/test.png"
    get_request(test_get_url)
    # post_json_request(test_post_json_url)
    # post_form_request(test_post_form_url)
    # upload_file(test_upload_url)
