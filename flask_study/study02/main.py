#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from flask import Flask, request

app = Flask(__name__)

"""
返回 html 网页
"""


@app.route("/t2", methods=["GET"])
def index():
    username = request.args.get("username")
    print(username)
    password = request.args.get("password")
    print(password)

    if username == "Lizhendong" and password == "123":
        return "<html><body>Welcome {username}</body></html>".format(username=username)
    else:
        return "<html><body>Welcome!</body></html>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)

# http://127.0.0.1:9000/t2?username=Lizhendong&password=123
