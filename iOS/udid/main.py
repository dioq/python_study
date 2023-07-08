#!/usr/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, request, send_from_directory

app = Flask(__name__)


@app.route("/install/<filename>", methods=["GET"])
def download(filename):
    return send_from_directory(path="files/", directory="./files/", filename=filename, as_attachment=True)


@app.route("/getuuid", methods=["GET"])
def plist():
    return send_from_directory(path="files/", directory="./files/", filename="udid.mobileconfig", as_attachment=True)


@app.route('/parse_udid', methods=['GET', 'POST'])
def parse_udid():
    """
    解析获取udid数据
    """
    new_test_str = str(request.data, encoding='utf-8')
    print(new_test_str)


# 实现通过浏览器下载并安装 安装包
if __name__ == "__main__":
    # iOS 13 后 ssl 证书必须得是 CA机构签发的
    app.run(host="0.0.0.0", port=9001, debug=True, ssl_context=('./cert/server.pem', './cert/server.key'))
