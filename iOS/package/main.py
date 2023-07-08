#!/usr/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("templates/index.html")  # 加入变量传递


@app.route("/install/<filename>", methods=["GET"])
def download(filename):
    return send_from_directory(path="files/", directory="./files/", filename=filename, as_attachment=True)


@app.route("/download.plist", methods=["GET"])
def plist():
    return send_from_directory(path="files/", directory="./files/", filename="download.plist", as_attachment=True)


# 实现通过浏览器下载并安装 安装包
if __name__ == "__main__":
    # iOS 13 后 ssl 证书必须得是 CA机构签发的
    app.run(host="0.0.0.0", port=9000, debug=True, ssl_context=('./cert/server.pem', './cert/server.key'))
