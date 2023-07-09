#!/usr/bin/python3
# -*- coding: utf-8 -*-
from pathlib import Path
from urllib import request

from flask import Flask, render_template, send_file, url_for, redirect

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
    # f = open("device.plist", "wb")
    # f.write(request.data)
    # f.close()
    # print("get_udid -------------> go here")

    global udid_l
    b_data = request.data
    data_str = str(b_data).split('<?xml')[-1].split('</plist>')[0].split('dict')[1].replace('\\n', '').replace('\\t',
                                                                                                               '') \
        .replace('>', '').replace('<', '').replace('/', '').replace('string', '').split('key')
    udid = data_str[4]
    print(udid)
    product = data_str[2]
    print(product)
    version = data_str[6]
    print(version)
    udid_l = [udid, product, version]
    # 这里一定要对301进行重定向
    return redirect(url_for('show_udid'), code=301)


# 实现通过浏览器下载并安装 安装包
if __name__ == "__main__":
    # iOS 13 后 ssl 证书必须得是 CA机构签发的
    app.run(host="0.0.0.0", port=9000, debug=True, ssl_context=('./cert/server.pem', './cert/server.key'))
