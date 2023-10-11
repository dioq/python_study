#!/usr/bin/python3
# -*- coding: utf-8 -*-
import qrcode
from MyQR import myqr
from PIL import Image


def QR_With_FullBackground_Img(link="https://jobs8.cn:9000",
                               background_picture="BackgroundIMG.png",
                               outputput_file="output_code_with_background_png.png"):
    # 图片布满整个二维码
    myqr.run(
        words=link,  # Link address
        version=1,  # 设置容错率为最高默认边长是取决于你输入的信息的长度和使用的纠错等级；而默认纠错等级是最高级的H
        level='H',  # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
        picture=background_picture,  # 用来将QR码图像与一张同目录下的图片相结合,产生一张黑白图片,格式可以是.jpg, .png, .bmp, .gif
        colorized=True,  # 可以使产生的图片由黑白(False)变为彩色(True)的
        contrast=1.0,  # 用以调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0。
        brightness=1.0,  # 用来调节图片的亮度
        save_name=outputput_file  # 输出文件名字
    )


def QR_With_Central_Img(link="https://jobs8.cn:9000",
                        central_picture="BackgroundIMG.png",
                        outputput_file="output_code_with_central_png.png"):
    # 图片在二维码中心位置
    qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image()
    img = img.convert("RGBA")
    icon = Image.open(central_picture)  # 这里是二维码中心的图片

    img_w, img_h = img.size
    factor = 4
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)

    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    icon = icon.convert("RGBA")
    img.paste(icon, (w, h), icon)
    img.save(outputput_file)
    # img.show()  # 显示图片,可以通过save保存


def QR_Single_Code(link="https://jobs8.cn:9000/", outputput_file="output_code_simple.png"):
    # 简单的二维码
    # 生成二维码实例，设置大小和边框
    qr = qrcode.QRCode(box_size=10, border=2)
    # 添加二维码的显示信息
    content = link
    qr.add_data(content)
    qr.make(fit=True)
    img = qr.make_image()
    # 保存二维码
    img.save(outputput_file)


if __name__ == '__main__':
    # link: url
    # background_picture: background picture filename
    # outputput_file: output filename
    url = "https://download.hanlee.net:3444"
    QR_With_FullBackground_Img(link=url, background_picture="BackgroundIMG.png",
                               outputput_file="output_code_with_background_png.png")

    # link: url
    # central_picture: central picture filename
    # outputput_file: output filename
    QR_With_Central_Img(link=url, central_picture="BackgroundIMG.png",
                        outputput_file="output_code_with_central_png.png")

    # link: url
    # outputput_file: output filename
    QR_Single_Code(link="itms-services://?action=download-manifest&url=https://jobs8.cn:9000/download.plist",
                   outputput_file="output_code_simple.png")
