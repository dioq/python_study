#!/usr/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

"""
往 html 中传数据
"""


@app.route('/<address>')
def test(address):
    return render_template("index.html", address=address, username="Lzd")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)

# http://127.0.0.1:9000/wuhan
