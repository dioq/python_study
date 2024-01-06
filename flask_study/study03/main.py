#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

"""
渲染 html
"""


@app.route('/t3')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)
