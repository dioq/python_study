#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from flask import Flask, request  # 导入Flask套件
import ssl  # SSL 证书

app = Flask(__name__)


def get_ssl_context():
    ca_file = "../cert/ca/ca.cer"
    cert_file = "../cert/server/server.cer"
    key_file = "../cert/server/server.key"

    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(
        certfile=cert_file, keyfile=key_file, password="C81FCCE046EE94EA"
    )
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE  # 单向验证, 客户端可以不上传自己的证书
    ssl_context.load_verify_locations(
        ca_file
    )  # 指定 CA 机构 验证 SSL证书, 如果不设置的话就使用系统默认的CA 此时SSL证书必须是官方机构颁发的才能通过验证

    return ssl_context


# 建立 giveGET 路由，回传 数据 和状态码 200
@app.route("/get", methods=["GET"])
def get_no_param():
    name_from_url = request.args.get(
        "name"
    )  # 获取 url 上传过来的参数,对 post请求也适用
    response_dict = {}
    if name_from_url is not None:
        print("args name:", name_from_url)
        response_dict["name"] = name_from_url
    response_dict["status"] = 200
    response_dict["msg"] = "Hello, This a message from server!"

    return response_dict, 200


@app.route("/post", methods=["POST"])
def post_param_json():
    # print('data:', request.data)
    params = request.get_json()  # 获取 json 格式数据
    # print("param json:\n", params)
    name = params["name"]  # 取其中的参数
    response_dict = {
        "status": 200,
        "name": name,
        "msg": "Hello,this is a message from server",
    }
    return response_dict, 200


if __name__ == "__main__":
    context = get_ssl_context()
    app.run(host="0.0.0.0", port=8091, debug=True, ssl_context=context)
