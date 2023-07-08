# -*- coding = utf-8 -*-
# ------------------------------
# @time: 2021/6/29 17:30
# @Author: drew_gg
# @File: get_ios_udid.py
# @Software: cover_app_platform
# ------------------------------

import os
from flask import Blueprint, request, render_template, redirect, url_for, Response
from app.common.common_ios_type import get_ios_type as ios_type

ios_udid = Blueprint('ios_udid', "__main__")

pl = os.getcwd().split('cover_app_platform')
xml_path = pl[0] + r'cover_app_platform\\app\\static\\xml\\'

# 定义全局变量
udid_l = []


@ios_udid.route('/index_udid/', methods=['GET', 'POST'])
def index_udid():
    """
    获取udid首页
    """
    return render_template('/post/get_udid/udid.html')


@ios_udid.route('/show_udid/', methods=['GET', 'POST'])
def show_udid():
    """
    展示获取到的udid页面
    """
    return render_template('/post/get_udid/show_udid.html', data=udid_l)


@ios_udid.route('/down_config/', methods=['GET', 'POST'])
def down_config():
    """
    ios设备访问下载配置文件
    """

    def file_content(f_p):
        with open(f_p, 'rb') as f:
            return f.readlines()

    file_path = xml_path + 'mobileconfig.xml'
    filename = os.path.basename(file_path)
    response = Response(file_content(file_path))
    # 这里的Content-Type一定要设置为application/x-apple-aspen-config
    response.headers['Content-Type'] = 'application/x-apple-aspen-config; chatset=utf-8'
    response.headers['Content-Disposition'] = 'attachment;filename="{}"'.format(filename)
    return response


@ios_udid.route('/get_udid/', methods=['GET', 'POST'])
def get_udid():
    """
    获取设备返回的值
    """
    global udid_l
    b_data = request.data
    data_str = str(b_data).split('<?xml')[-1].split('</plist>')[0].split('dict')[1].replace('\\n', '').replace('\\t',
                                                                                                               '') \
        .replace('>', '').replace('<', '').replace('/', '').replace('string', '').split('key')
    udid = data_str[4]
    product = ios_type.get_phone(data_str[2])
    version = data_str[6]
    udid_l = [udid, product, version]
    # 这里一定要对301进行重定向
    return redirect(url_for('ios_udid.show_udid'), code=301)


    # -*- coding = utf-8 -*-
    # ------------------------------
    # @time: 2021/7/1 5:18 PM
    # @Author: drew_gg
    # @File: get_ios_type.py
    # @Software: FM_APP_PKG
    # ------------------------------


def get_phone(ios_type):
    if ios_type in ["iPhone3,1", "iPhone3,2", "iPhone3,3"]:
        return "iPhone 4"
    if ios_type in ["iPhone4,1"]:
        return "iPhone 4s"
    if ios_type in ["iPhone5,1", "iPhone5,2"]:
        return "iPhone 5"
    if ios_type in ["iPhone5,3", "iPhone5,4"]:
        return "iPhone 5c"
    if ios_type in ["iPhone6,1", "iPhone6,2"]:
        return "iPhone 5s"
    if ios_type in ["iPhone7,2"]:
        return "iPhone 6"
    if ios_type in ["iPhone7,1"]:
        return "iPhone 6 Plus"
    if ios_type in ["iPhone8,1"]:
        return "iPhone 6s"
    if ios_type in ["iPhone8,2"]:
        return "iPhone 6s Plus"
    if ios_type in ["iPhone8,3"]:
        return "iPhone SE (GSM+CDMA)"
    if ios_type in ["iPhone8,4"]:
        return "iPhone SE (GSM)"
    if ios_type in ["iPhone9,1"]:
        return "iPhone 7 (CDMA)"
    if ios_type in ["iPhone9,2"]:
        return "iPhone 7 Plus (CDMA)"
    if ios_type in ["iPhone9,3"]:
        return "iPhone 7 (GSM)"
    if ios_type in ["iPhone9,4"]:
        return "iPhone 7 Plus (GSM)"
    if ios_type in ["iPhone10,1"]:
        return "iPhone 8 (CDMA)"
    if ios_type in ["iPhone10,2"]:
        return "iPhone 8 Plus (CDMA)"
    if ios_type in ["iPhone10,3"]:
        return "iPhone X (CDMA)"
    if ios_type in ["iPhone10,4"]:
        return "iPhone 8 (GSM)"
    if ios_type in ["iPhone10,5"]:
        return "iPhone 8 Plus (GSM)"
    if ios_type in ["iPhone10,6"]:
        return "iPhone X (GSM)"
    if ios_type in ["iPhone11,2"]:
        return "iPhone XS"
    if ios_type in ["iPhone11,4"]:
        return "iPhone XS Max China"
    if ios_type in ["iPhone11,6"]:
        return "iPhone XS Max"
    if ios_type in ["iPhone11,8"]:
        return "iPhone XR"
    if ios_type in ["iPhone12,1"]:
        return "iPhone 11"
    if ios_type in ["iPhone12,3"]:
        return "iPhone 11 Pro"
    if ios_type in ["iPhone12,5"]:
        return "iPhone 11 Pro Max"
    if ios_type in ["iPhone12,8"]:
        return "iPhone SE 2nd Gen"
    if ios_type in ["iPhone13,1"]:
        return "iPhone 12 mini"
    if ios_type in ["iPhone13,2"]:
        return "iPhone 12"
    if ios_type in ["iPhone13,3"]:
        return "iPhone 12 Pro"
    if ios_type in ["iPhone13,4"]:
        return "iPhone 12 Pro Max"
    if ios_type in ["i386", "x86_64"]:
        return "Simulator"
    else:
        return "I do not know !"


# 实现通过浏览器下载并安装 安装包
if __name__ == "__main__":
    # iOS 13 后 ssl 证书必须得是 CA机构签发的
    ios_udid.run(host="0.0.0.0", port=9000, debug=True, ssl_context=('./cert/server.pem', './cert/server.key'))
