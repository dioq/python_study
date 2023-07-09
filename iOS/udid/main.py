#!/usr/bin/python3
# -*- coding: utf-8 -*-
from pathlib import Path

from flask import Flask, render_template, send_file, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    path = "index.html"
    return render_template(path)  # 加入变量传递


@app.route("/download/<filename>", methods=["GET"])
def download(filename):
    print("download ---------> go here || " + filename)
    file_path = "./files/" + filename
    file = Path(file_path)
    return send_file(file, as_attachment=True)


@app.route('/get_udid', methods=['GET', 'POST'])
def get_udid():
    """
    获取设备返回的值
    """
    f = open("device.xml", "wb")
    f.write(request.data)
    f.close()

    global device_info
    b_data = request.data
    data_str = str(b_data).split('<?xml')[-1].split('</plist>')[0].split('dict')[1].replace('\\n', '').replace('\\t',
                                                                                                               '') \
        .replace('>', '').replace('<', '').replace('/', '').replace('string', '').split('key')
    udid = data_str[4]
    print("udid:" + udid)
    product = data_str[2]
    print("product:" + product)
    version = data_str[6]
    print("version:" + version)
    device_info = [udid, product, version]
    # 这里一定要对301进行重定向
    return redirect(url_for('show_udid'), code=301)


@app.route('/show_udid', methods=['GET', 'POST'])
def show_udid():
    """
    展示获取到的udid页面
    """
    path = "show_udid.html"
    return render_template(path, udid=device_info[0], product=device_info[1], version=device_info[2])


# 实现通过浏览器下载并安装 安装包
if __name__ == "__main__":
    # iOS 13 后 ssl 证书必须得是 CA机构签发的
    app.run(host="0.0.0.0", port=9000, debug=True, ssl_context=('./cert/server.pem', './cert/server.key'))
