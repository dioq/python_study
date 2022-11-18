#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 导入Flask套件
from flask import Flask, request

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


# 建立根目錄路由，並輸出文字
@app.route("/", methods=['GET'])
def giveHtml():
    return "<h1>Hello , This a Restful Api Server by Flask...</h1>"


# 建立 giveGET 路由，回传 数据 和状态码 200
@app.route("/get", methods=['GET'])
def getNoParam():
    name = request.args.get('name')
    if name == None:
        name = "Noname"
    print(name)
    item = {'name': name, 'output': output}
    return item, 200


@app.route("/post", methods=['POST'])
def postParamAsJson():
    print('data:', request.data)
    params = request.get_json()  # 获取 json 格式数据
    print("param json:\n", params)
    name = params["name"]  # 取其中的参数
    item = {'name': name, 'output': output}
    # output.append(params)
    return item, 200


@app.route("/postform", methods=['POST'])
def postParamAsForm():
    name = request.args.get('name')
    print(name)
    item = {'name': name, 'output': output}
    return item, 200


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=True)
