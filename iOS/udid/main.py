#!/usr/bin/python3
# -*- coding: utf-8 -*-
from pathlib import Path

from flask import Flask, render_template, send_file, make_response, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    path = "templates/index.html"
    return render_template(path)  # 加入变量传递


@app.route("/download/<filename>", methods=["GET"])
def download(filename):
    print("download ---------> go here || " + filename)
    file_path = "./files/" + filename
    file = Path(file_path)
    return send_file(file, as_attachment=True)


@app.route('/down_config', methods=['GET', 'POST'])
def down_config():
    """
    ios设备访问下载配置文件
    """
    print("down_config ---------> go here")

    # def file_content(f_p):
    #     with open(f_p, 'rb') as f:
    #         return f.readlines()
    #
    filename = "mobileconfig.xml"
    file_path = "./files/mobileconfig.xml"
    # response = Response(file_content(file_path))
    # print(response)
    f = open(file_path, "r")
    lines = f.read()
    print(lines)
    print(type(lines))
    response = make_response(lines)
    # 这里的Content-Type一定要设置为application/x-apple-aspen-config
    response.headers['Content-Type'] = 'application/x-apple-aspen-config; chatset=utf-8'
    response.headers['Content-Disposition'] = 'attachment;filename="{}"'.format(filename)
    print(response)

    f.close()
    return response


# @app.route("/get_udid", methods=["GET", "POST"])
# def get_udid():
#     print(request.data)
#
#     new_test_str = str(request.data, encoding='utf-8')
#     print(new_test_str)
#     return "hello, go here"



@app.route('/get_udid', methods=['GET', 'POST'])
def get_udid():
    """
    获取设备返回的值
    """
    # f = open("device.plist", "wb")
    # f.write(request.data)
    # f.close()
    print("get_udid -------------> go here")

    global udid_l
    b_data = request.data
    data_str = str(b_data).split('<?xml')[-1].split('</plist>')[0].split('dict')[1].replace('\\n', '').replace('\\t',
                                                                                                               '') \
        .replace('>', '').replace('<', '').replace('/', '').replace('string', '').split('key')
    udid = data_str[4]
    product = "iPhone 7"
    version = data_str[6]
    udid_l = [udid, product, version]
    # 这里一定要对301进行重定向
    return redirect(url_for('show_udid'), code=301)


@app.route('/show_udid', methods=['GET', 'POST'])
def show_udid():
    """
    展示获取到的udid页面
    """
    path = "show_udid.html"
    return render_template(path, data=udid_l)


# 实现通过浏览器下载并安装 安装包
if __name__ == "__main__":
    # iOS 13 后 ssl 证书必须得是 CA机构签发的
    app.run(host="0.0.0.0", port=9000, debug=True, ssl_context=('./cert/server.pem', './cert/server.key'))
