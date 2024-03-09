#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import urllib.request
import ssl

# url_prefix = "https://jobs8.cn:8091"
url_prefix = "https://127.0.0.1:8091"
https_get_url = url_prefix + "/get"
https_post_url = url_prefix + "/post"


# 设置 SSLContext
def get_ssl_context():
    ca_file = "../cert/ca/ca.cer"
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_context.check_hostname = False  # 是否验证域名
    ssl_context.verify_mode = ssl.CERT_REQUIRED  # 对方必须 上传 ssl 证书 让自己验证
    ssl_context.load_verify_locations(
        ca_file
    )  # 指定 CA 机构 验证 SSL证书, 如果不设置的话就使用系统默认的CA 此时SSL证书必须是官方机构颁发的才能通过验证

    return ssl_context


# 测试 get 请求
def get_func():
    context = get_ssl_context()

    try:
        request = urllib.request.Request(https_get_url)
        res = urllib.request.urlopen(request, context=context)
        print(res.code)
        print(res.read().decode("utf-8"))
    except Exception as ex:
        print("Found Error in auth phase:%s" % str(ex))


# 测试 post 请求 参数为 json
def post_func():
    context = get_ssl_context()

    headers = {
        "User-Agent": "iOS",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Connection": "keep-alive",
    }
    param_str = '{"name": "JOJO999","age": 18}'
    data_bytes = param_str.encode("utf-8")
    try:
        request = urllib.request.Request(
            url=https_post_url, data=data_bytes, headers=headers
        )
        res = urllib.request.urlopen(request, context=context)
        print(res.code)
        print(res.read().decode("utf-8"))
    except Exception as ex:
        print("Found Error in auth phase:%s" % str(ex))


if __name__ == "__main__":
    get_func()
    post_func()
