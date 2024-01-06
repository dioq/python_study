#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from pathlib import Path

from flask import Flask, render_template, send_file, request, redirect, url_for

import CryptoUtil

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


@app.route('/get_udid', methods=['GET', 'POST'])
def get_udid():
    """
    获取设备返回的值
    """
    global dict
    data = CryptoUtil.extract_data(request.data)
    dict = CryptoUtil.parse_plist(data)

    # 这里一定要对301进行重定向
    return redirect(url_for('show_udid'), code=301)


@app.route('/show_udid', methods=['GET', 'POST'])
def show_udid():
    """
    展示获取到的udid页面
    """

    exist = dict.__contains__("IMEI")
    if exist:
        IMEI = dict["IMEI"]
    else:
        IMEI = "null"

    path = "show_udid.html"
    return render_template(path, udid=dict["UDID"], product=dict["PRODUCT"], version=dict["VERSION"], IMEI=IMEI)


# 实现通过浏览器下载并安装 安装包
if __name__ == "__main__":
    # iOS 13 后 ssl 证书必须得是 CA机构签发的
    app.run(host="0.0.0.0", port=9000, debug=True, ssl_context=('./cert/server.pem', './cert/server.key'))
