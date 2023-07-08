#!/usr/bin/python3
# -*- coding: utf-8 -*-
from pathlib import Path

import requests
from flask import Flask, render_template, send_file, Response, request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    path = "index.html"
    return render_template(path)  # 加入变量传递


@app.route("/download/<filename>", methods=["GET"])
def download(filename):
    file_path = "./files/" + filename
    file = Path(file_path)
    return send_file(file, as_attachment=True)


@app.route('/down_config/', methods=['GET', 'POST'])
def down_config():
    """
    ios设备访问下载配置文件
    """

    def file_content(f_p):
        with open(f_p, 'rb') as f:
            return f.readlines()

    filename = "udid.mobileconfig"
    file_path = "./files/udid.mobileconfig"
    response = Response(file_content(file_path))
    print(response)
    # 这里的Content-Type一定要设置为application/x-apple-aspen-config
    response.headers['Content-Type'] = 'application/x-apple-aspen-config; chatset=utf-8'
    response.headers['Content-Disposition'] = 'attachment;filename="{}"'.format(filename)
    print(response)
    return response


@app.route("/get_udid", methods=["GET", "POST"])
def get_udid():
    print(request.data)
    new_test_str = str(request.data, encoding='utf-8')
    print(new_test_str)


# 实现通过浏览器下载并安装 安装包
if __name__ == "__main__":
    # iOS 13 后 ssl 证书必须得是 CA机构签发的
    app.run(host="0.0.0.0", port=9000, debug=True, ssl_context=('./cert/server.pem', './cert/server.key'))