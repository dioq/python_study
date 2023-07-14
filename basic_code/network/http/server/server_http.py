#!/usr/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, request, send_file  # 导入Flask套件
import json  # 处理 json 数据

app = Flask(__name__)  # 创建Flask app物件


# 接口 get
@app.route("/get", methods=['GET'])
def get_test():
    name_from_url = request.args.get('name')  # 获取 url 上传过来的参数,对 post请求也适用
    response_dict = {}
    if name_from_url is not None:
        print("args name:", name_from_url)
        response_dict["name"] = name_from_url
    response_dict["status"] = 200
    response_dict["msg"] = "Hello, This a message from server!"

    return response_dict, 200


# 接口 post, body 格式为 json
@app.route("/post", methods=['POST'])
def post_test():
    print("request.data:", request.data)  # 传过来的 binary data

    # body 数据解析成 json
    # json_dict = request.get_json()
    json_str = str(request.data, encoding='utf-8')
    json_dict = json.loads(json_str)
    # print("json_dict:\n",  json_dict)
    # 获取 body 中的参数 address
    address = json_dict["address"]
    print("param from body json:" + address)

    response_dict = {"status": 200, "address": address, "msg": "Hello, This a message from server!"}
    return response_dict, 200


# 接口 post, body 格式为 form
@app.route("/postform", methods=['POST'])
def post_form_test():
    print("request.data:", request.data)
    print("request.form:", request.form)

    # body 从 body 里提取 form 数据
    address = request.form["address"]
    print("param from body form:" + address)

    response_dict = {"status": 200, "address": address, "msg": "Hello, This a message from server!"}
    return response_dict, 200


# 上传文件
@app.route('/upload', methods=['POST'])
def upload():
    print("Posted file: {}".format(request.files['file']))
    file_storage = request.files['file']  # 获取上传过来的文件数据
    file_name = file_storage.filename  # 上传的文件名
    file_path = "./files/" + file_name  # 文件在服务器保存的路径
    file_storage.save(file_path)  # 文件数据保存到磁盘

    response_dict = {"status": 200, "msg": "file uploaded successfully!"}
    return response_dict, 200


# 下载文件
@app.route("/download/<filename>", methods=["GET"])
def download(filename):
    response_dict = {}
    if filename is None:
        response_dict["status"] = -10
        response_dict["msg"] = "File name is null"
        return response_dict

    file_path = "./files/" + filename
    return send_file(file_path, as_attachment=True)


# 显示图片
@app.route("/image/<filename>", methods=['GET'])
def show_image(filename):
    file_path = "./files/" + filename
    # as_attachment : True 下载文件, False 不下载文件
    return send_file(file_path, as_attachment=False)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=True)
