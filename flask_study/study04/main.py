#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

"""
往 html 中传数据
"""


@app.route('/t4')
def test():
    t_int = 18
    t_str = 'curry'
    t_list = [1, 4, 3, 2]
    t_dict = {
        'name': 'Diamon',
        'age': 27
    }

    return render_template("index.html", my_int=t_int, my_str=t_str, my_list=t_list, my_dict=t_dict)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)

# http://127.0.0.1:9000/t4
