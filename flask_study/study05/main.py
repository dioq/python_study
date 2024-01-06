#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/admin')
def func_admin():
    return 'Admin'


@app.route('/guest/<guest>')
def func_guest(guest):
    # return 'Log in as Guest %s' % guest
    return "Log in as Guest {Guest}".format(Guest=guest)


@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        # 重定向到 func_admin 方法
        return redirect(url_for('func_admin'))
    else:
        # 重定向到 func_guest 方法, 参数为 name
        return redirect(url_for('func_guest', guest=name))


if __name__ == "__main__":
    app.run(debug=True, threaded=True)

# http://127.0.0.1:5000/user/admin
# http://127.0.0.1:5000/user/jojo
