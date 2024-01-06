#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

"""
html 页面跳转
"""


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            return redirect(url_for('success'))
        else:
            return "登录错误"
    elif request.method == 'GET':
        return redirect(url_for('index'))


@app.route('/succes')
def success():
    return 'logged in successfully'


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
