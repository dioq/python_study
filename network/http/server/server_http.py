#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 导入Flask套件
from flask import Flask, request, send_from_directory

"""
pip install -U Flask 
"""

# 处理上传的文件
import os
from werkzeug.utils import secure_filename

# 创建Flask app物件
app = Flask(__name__)

# 创建 output 输出内容
output = [
    {
        "pid": "1",
        "title": "Example01",
        "price": 10,
        "img": "https://picsum.photos/id/999/1200/600",
        "isAvailable": True
    },
    {
        "id": "2",
        "title": "Example02",
        "price": 60,
        "img": "https://picsum.photos/id/1070/1200/600",
        "isAvailable": True
    }
]


# 测接口 get
@app.route("/get", methods=['GET'])
def getTest():
    name = request.args.get('name')  # 获取 url 上传过来的参数,对 post请求也适用
    if name is None:
        name = "Noname"
    print(name)
    item = {'name': name, 'output': output}
    return item, 200


# 测接口 post
@app.route("/post", methods=['POST'])
def postParamAsJson():
    name1 = request.args.get('name')  # 获取 url 上传过来的参数,对 post请求也适用

    print("args name1:", name1)
    print("request.data:", request.data)
    params_json = request.get_json()  # 获取 json 格式数据
    print("request.get_json():\n", params_json)
    name = params_json["name"]  # 取其中的参数
    if name1 is not None:
        name = name1 + name
    item = {'name': name, 'output': output}
    return item, 200


# 测接口 上传文件
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        # print(request.files)
        # 参数: 1.保存路径    2.文件大小
        f.save(os.path.join("files", secure_filename(f.filename)))
        return 'file uploaded successfully', 200

    if request.method == 'GET':
        return "上传文件需要用 post!", 203


# 测接口 显示图片
@app.route("/<filename>", methods=['GET', 'POST'])
def download2(filename):
    # as_attachment : True 下载文件, False 不下载文件
    return send_from_directory(path="./files/", directory="./files/", filename=filename, as_attachment=False)


# 测接口 下载文件
@app.route("/download", methods=['GET', 'POST'])
def download():
    name = request.args.get('name')  # 获取 url 上传过来的参数,对 post请求也适用
    if name is None:
        name = "test.ipa"
    return send_from_directory(path="./files/", directory="./files/", filename=name, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=True)
