#!/usr/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

"""
css js 的使用
"""


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == "123456":
        return redirect(url_for('success'))
    else:
        return "登录错误"


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route('/forgot_pwd', methods=['GET', 'POST'])
def forgot_pwd():
    return render_template('password.html')


@app.route('/forgot_pwd2', methods=['GET', 'POST'])
def forgot_pwd2():
    return render_template('password_2.html')


@app.route('/forgot_pwd3', methods=['GET', 'POST'])
def forgot_pwd3():
    return render_template('password_3.html')


@app.route('/succes')
def success():
    return render_template('register_succ.html')


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
