#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 載入必須套件
from flask import Flask, request
from flask_restful import Resource, Api

# 創建Flask app物件
app = Flask(__name__)
api = Api(app)

# 創建一個陣列(創一個名為apple物品當測試)，存放品項
items = [
    {
        "name": "apple",
        "price": 32.3
    }
]


class PostJSON(Resource):

    # 建制新品項
    def post(self):
        # 如果該品項不存在，則解析客戶端傳來的body，並將其品項寫入 items
        params = request.get_json()
        print("param json:\n", params)
        item = {'name': "Dio", 'price': params['price']}
        items.append(item)
        return item, 200


class PostFromdata(Resource):

    def post(self):
        # 如果該品項不存在，則解析客戶端傳來的body，並將其品項寫入 items
        params = request.form
        print(params)
        item = {'name': "Dio", 'price': 39.0}
        items.append(item)
        return items, 200


api.add_resource(PostJSON, '/post')
api.add_resource(PostFromdata, '/postformdata')


if __name__ == "__main__":
    app.run(port=8088, debug=True)
