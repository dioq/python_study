#!/usr/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, make_response

app = Flask(__name__)

"""
路由演示
"""

@app.route('/')
def index():
    response = make_response("Hello, 梦想橡皮擦")
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response


@app.route('/t1')
def test02():
    test_str = "abcdef"
    # 字符串转成 byte数组
    test_bytes = bytes(test_str, encoding="utf8")
    response = make_response(test_bytes)
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000, debug=True)
