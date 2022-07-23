#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request

import ssl


def getSSLContext():
    CA_FILE = "../cert/ca/ca.cer"
    KEY_FILE = "../cert/client/client.key"
    CERT_FILE = "../cert/client/client.cer"

    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.check_hostname = False
    context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
    context.load_verify_locations(CA_FILE)
    context.verify_mode = ssl.CERT_REQUIRED # 对方必须 上传 ssl 证书 让自己验证
    # 证书密码:zxcvbnm,.

    return context


if __name__ == '__main__':
    context = getSSLContext()
    try:
        request = urllib.request.Request('https://127.0.0.1:8091/get')
        res = urllib.request.urlopen(request, context=context)
        print(res.code)
        print(res.read().decode("utf-8"))
    except Exception as ex:
        print("Found Error in auth phase:%s" % str(ex))
