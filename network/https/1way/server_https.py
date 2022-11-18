#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 导入Flask套件
from flask import Flask, request
# SSL 证书
import ssl

# 创建Flask app物件
app = Flask(__name__)


def getSSLContext():
    CA_FILE = "../cert/ca/ca.cer"
    KEY_FILE = "../cert/server/server.key"
    CERT_FILE = "../cert/server/server.cer"

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.check_hostname = False
    context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE, password="zxcvbnm,.")
    context.load_verify_locations(CA_FILE)
    context.verify_mode = ssl.CERT_OPTIONAL  # 单向验证, 客户端可以不上传自己的证书
    # 证书密码:zxcvbnm,.

    return context


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


@app.route("/post", methods=['POST'])
def postParamAsJson():
    print('data:', request.data)
    params = request.get_json()  # 获取 json 格式数据
    print("param json:\n", params)
    name = params["name"]  # 取其中的参数
    item = {'name': name, 'output': output}
    # output.append(params)
    return item, 200


if __name__ == "__main__":
    context = getSSLContext()
    app.run(host="0.0.0.0", port=8091, debug=True, ssl_context=context)
