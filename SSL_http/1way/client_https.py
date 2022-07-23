#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request

import ssl

'''
SSL 单向验证, client 验证一下服务器传过来的证书 是不是 CA 机构颁发的. 客户端 是不用上传自己的证书的
'''

# 自己创建的 CA
def getSSLContext():
    CA_FILE = "../cert/ca/ca.cer"
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.check_hostname = False
    context.load_verify_locations(CA_FILE)
    context.verify_mode = ssl.CERT_REQUIRED # 对方必须 上传 ssl 证书 让自己验证

    return context

# 系统默认的 CA
def ignoreSSLContext():
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    return context


if __name__ == '__main__':

    # 验证 服务器证书是否是 CA 证书
    context = getSSLContext()
    # 单向验证 可以忽略证书
    # context = ignoreSSLContext()

    try:
        request = urllib.request.Request('https://127.0.0.1:8091/get')
        res = urllib.request.urlopen(request, context=context)
        print(res.code)
        print(res.read().decode("utf-8"))
    except Exception as ex:
        print("Found Error in auth phase:%s" % str(ex))
