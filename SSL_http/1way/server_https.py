#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 导入Flask套件
from flask import Flask
# SSL 证书
import ssl

# 创建Flask app物件
app = Flask(__name__)

# 创建 output 输出内容
output = [
    {
        "pid": "1",
        "title": "Example01",
        "price": 10,
        "img": "https://picsum.photos/id/999/1200/600",
        "isAvailable": True
    },
    {
        "id": "2",
        "title": "Example02",
        "price": 60,
        "img": "https://picsum.photos/id/1070/1200/600",
        "isAvailable": True
    }
]


# 建立 giveGET 路由，回传 数据 和状态码 200
@app.route("/get", methods=['GET'])
def getNoParam():
    return {"products": {"Message": "get request is suucess!", "output": output}}, 200


def getSSLContext():
    CA_FILE = "../cert/ca/ca.cer"
    KEY_FILE = "../cert/server/server.key"
    CERT_FILE = "../cert/server/server.cer"

    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.check_hostname = False
    context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
    context.load_verify_locations(CA_FILE)
    context.verify_mode = ssl.CERT_OPTIONAL  # 单向验证, 客户端可以不上传自己的证书
    # 证书密码:zxcvbnm,.

    return context

if __name__ == "__main__":

    context = getSSLContext()
    app.run(port=8091, debug=True, ssl_context=context)
