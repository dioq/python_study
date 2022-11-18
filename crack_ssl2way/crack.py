#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import ssl

url_ssl = "https://jobs8.cn:8083/getdata"

'''
破解双向验证:
上面这个 https 网络请求是 ssl双向验证的, 是Android 端与服务器通讯. 要想成功逆出这个协议,必须在Android 客户端找到 client 证书,
因为这个Android app 是我写的，我直接把 client.p12 证书取出来(密码可以hook出来 是 changeit)，如果是 java 来实现话直接用client.p12 和
密码就能重发网络请求了。但是python 加载不了 p12证书,我只好用 openssl 把 client.p12 转化成 client.pem 证书和 client.key
拿着这个证书和密钥就可以在python里 与服务器通讯了
转化过程:
openssl pkcs12 -in client.p12  -out client.pem -nodes
openssl pkcs12 -in client.p12 -nocerts -nodes -out client.key

关于不同格式的证书的介绍可以看这里:https://developer.aliyun.com/article/557231
'''

# 获取自己的 ssl 证书
def getSSLContext():
    # CA_FILE = "../https/cert/ca/ca.cer"
    KEY_FILE = "client.key"
    CERT_FILE = "client.pem"

    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.check_hostname = False
    context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
    # context.load_verify_locations(CA_FILE)
    context.verify_mode = ssl.CERT_NONE # 不验证服务器端的证书
    # 证书密码:zxcvbnm,.

    return context


# 忽略证书
def ignoreSSLContext():
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    return context


if __name__ == '__main__':
    context = getSSLContext()
    # context = ignoreSSLContext()

    try:
        request = urllib.request.Request(url_ssl)
        res = urllib.request.urlopen(request, context=context)
        print(res.code)
        print(res.read().decode("utf-8"))
    except Exception as ex:
        print("Found Error in auth phase:%s" % str(ex))

    # requests.get(url_ssl, verify='test/client.pem')
