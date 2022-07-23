#!/usr/bin/python3

import requests

http_get_url = "http://jobs8.cn:8081/getdata"
http_post_url = "http://jobs8.cn:8081/postdata"
http_post_formdata_url = "http://jobs8.cn:8081/formdata"


# 测试 get 请求
def getFunc():
    response = requests.get(http_get_url)
    if (response.status_code == 200):
        print("请求成功!")
        print(response.text)
    else:
        print(response.status_code)
        print("请求失败!")


# 测试 post 请求 参数为 json
def postFunc():
    param = {"name": "JOJO", "age": 25}
    print(param)
    response = requests.post(http_post_url, json=param, verify=False) # 不验证 服务器 ssl 证书
    if (response.status_code == 200):
        print("请求成功!")
        print(response.text)
    else:
        print(response.status_code)
        print("请求失败!")


# 测试 post 请求 参数为 formdata
def postFormdataFunc():
    headers = {
        "content-type": "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW"
    }
    params = "name=JOJO&age=25"
    # print(params)
    response = requests.post(http_post_formdata_url, params=params, headers=headers)
    if (response.status_code == 200):
        print("请求成功!")
        print(response.text)
    else:
        print(response.status_code)
        print("请求失败!")


if __name__ == "__main__":
    # getFunc()
    # postFunc()
    postFormdataFunc()
