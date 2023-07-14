#!/usr/bin/python3
# -*- coding: utf-8 -*-
import urllib.request
import ssl

# url_prefix = "https://jobs8.cn:8091"
url_prefix = "https://127.0.0.1:8091"
https_get_url = url_prefix + "/get"
https_post_url = url_prefix + "/post"

'''
SSL 单向验证, client 验证一下服务器传过来的证书 是不是 CA 机构颁发的. 客户端 是不用上传自己的证书的
'''


# 自己创建的 CA
def custom_ssl_context():
    ca_file = "../cert/ca/ca.cer"
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_context.check_hostname = False  # 是否验证域名
    ssl_context.load_verify_locations(ca_file)  # 验证 SSL证书 所用CA
    ssl_context.verify_mode = ssl.CERT_REQUIRED  # 对方必须 上传 ssl 证书 让自己验证

    return ssl_context


# 系统默认的 CA
def system_ssl_context():
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_REQUIRED  # 对方必须 上传 ssl 证书 让自己验证

    return ssl_context


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
    # 单向验证 服务器证书是否是 CA 证书
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
