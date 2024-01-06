#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from flask import Flask, render_template, request

app = Flask(__name__)

"""
html 表单发送到模板
"""


@app.route('/')
def student():
    return render_template('index.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        rst = request.form
        return render_template("result.html", result=rst)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
