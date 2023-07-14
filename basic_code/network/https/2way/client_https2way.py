#!/usr/bin/python3
# -*- coding: utf-8 -*-
import urllib.request
import ssl

# url_prefix = "https://jobs8.cn:8092"
url_prefix = "https://127.0.0.1:8092"
https_get_url = url_prefix + "/get"
https_post_url = url_prefix + "/post"


def custom_ssl_context():
    ca_file = "../cert/ca/ca.cer"
    cert_file = "../cert/client/client.cer"
    key_file = "../cert/client/client.key"

    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_context.check_hostname = False
    ssl_context.load_cert_chain(certfile=cert_file, keyfile=key_file, password="9DB48AA87C9FFBCA")
    ssl_context.load_verify_locations(ca_file)
    ssl_context.verify_mode = ssl.CERT_REQUIRED  # Server 必须 传送 ssl 证书 让自己验证

    return ssl_context


# 系统默认的 CA
def system_ssl_context():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_REQUIRED  # 对方必须 上传 ssl 证书 让自己验证

    return context


# 测试 get 请求
def get_func():
    # 单向验证 服务器证书是否是 CA 签发的
    # context = system_ssl_context() # SSL 证书得是CA机构颁发的
    context = custom_ssl_context()  # SSL 证书 是自己模拟的 CA 签发的

    try:
        request = urllib.request.Request(https_get_url)
        res = urllib.request.urlopen(request, context=context)
        print(res.code)
        print(res.read().decode("utf-8"))
    except Exception as ex:
        print("Found Error in auth phase:%s" % str(ex))


# 测试 post 请求 参数为 json
def post_func():
    # 单向验证 服务器证书是否是 CA 签发的
    # context = system_ssl_context() # SSL 证书得是CA机构颁发的
    context = custom_ssl_context()  # SSL 证书 是自己模拟的 CA 签发的

    headers = {
        "User-Agent": "iOS",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Connection": "keep-alive"
    }
    param_str = "{\"name\": \"JOJO999\",\"age\": 18}"
    data_bytes = param_str.encode('utf-8')
    try:
        request = urllib.request.Request(url=https_post_url, data=data_bytes, headers=headers)
        res = urllib.request.urlopen(request, context=context)
        print(res.code)
        print(res.read().decode("utf-8"))
    except Exception as ex:
        print("Found Error in auth phase:%s" % str(ex))


if __name__ == '__main__':
    get_func()
    post_func()
