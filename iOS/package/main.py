#!/usr/bin/python3
# -*- coding: utf-8 -*-
from pathlib import Path
from urllib import request

from flask import Flask, render_template, send_file

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
    app.run(host="0.0.0.0", port=9000, debug=True, ssl_context=('./cert/server.pem', './cert/server.key'))
