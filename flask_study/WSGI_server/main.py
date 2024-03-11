#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from flask import Flask, make_response
from gevent import pywsgi
import gevent.ssl as ssl  # gevent 自带的ssl库 与gevent兼容性更好些

# import ssl  # SSL 证书

app = Flask(__name__)


def get_ssl_context():
    ca_file = "./cert/ca/ca.cer"
    cert_file = "./cert/server/server.cer"
    key_file = "./cert/server/server.key"

    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(
        certfile=cert_file, keyfile=key_file, password="C81FCCE046EE94EA"
    )
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE  # 单向验证, 客户端可以不上传自己的证书
    ssl_context.load_verify_locations(ca_file)

    return ssl_context


@app.route("/test")
def test02():
    content = "This is a test message."
    # 字符串转成 byte数组
    test_bytes = bytes(content, encoding="utf8")
    response = make_response(test_bytes)
    response.headers["Content-Type"] = "text/html; charset=utf-8"
    return response


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=9000, debug=True)
    # app.run(host="0.0.0.0", port=9000, debug=True, ssl_context=get_ssl_context())
    # server = pywsgi.WSGIServer(("0.0.0.0", 9000), app)  # 不添加 SSL 证书
    server = pywsgi.WSGIServer(("0.0.0.0", 9000), app, ssl_context=get_ssl_context())
    server.serve_forever()
