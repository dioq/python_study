#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import ssl

# https_get_url = "https://jobs8.cn:8092/get"
https_get_url = "https://127.0.0.1:8092/get"
https_post_url = "https://127.0.0.1:8092/post"


def getSSLContext():
    CA_FILE = "../cert/ca/ca.cer"
    KEY_FILE = "../cert/client/client.key"
    CERT_FILE = "../cert/client/client.cer"

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.check_hostname = False
    context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE, password="zxcvbnm,.")
    context.load_verify_locations(CA_FILE)
    context.verify_mode = ssl.CERT_REQUIRED  # 对方必须 上传 ssl 证书 让自己验证
    # 证书密码:zxcvbnm,.

    return context


# 测试 get 请求
def getFunc():
    # 验证 服务器证书是否是 CA 证书
    context = getSSLContext()
    # 单向验证 可以忽略证书
    # context = ignoreSSLContext()

    try:
        request = urllib.request.Request(https_get_url)
        res = urllib.request.urlopen(request, context=context)
        print(res.code)
        print(res.read().decode("utf-8"))
    except Exception as ex:
        print("Found Error in auth phase:%s" % str(ex))


# 测试 post 请求 参数为 json
def postFunc():
    # 验证 服务器证书是否是 CA 证书
    context = getSSLContext()

    headers = {
        "User-Agent": "iOS",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Connection": "keep-alive"
    }
    data = "{\"name\": \"JOJO999\",\"age\": 18}"
    datas = data.encode('utf-8')
    try:
        request = urllib.request.Request(url=https_post_url, data=datas, headers=headers)
        res = urllib.request.urlopen(request, context=context)
        print(res.code)
        print(res.read().decode("utf-8"))
    except Exception as ex:
        print("Found Error in auth phase:%s" % str(ex))


if __name__ == '__main__':
    getFunc()
    # postFunc()
