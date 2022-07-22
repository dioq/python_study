import json
import os

from requests_toolbelt import MultipartEncoder
import requests

url = "http://hk.hanlee.top:58002/api/ios/saveregaccount"
wx_file_path="./wx.dat"
num = 0

def sumbit_wxInfo():
    m = MultipartEncoder(
        fields={'wxuser': 'name1',
                'wxpwd': 'pwd11111',
                'wxid': '131313244',
                'file': ('wx.dat', open(wx_file_path, 'rb'), 'text/plain')}
    )

    r = requests.post(url,data=m,headers={'Content-Type': m.content_type})
    # print(r.text)
    return r

def check_submit() :
    print("上传文件 ...")
    r = sumbit_wxInfo()
    if r.status_code != 200:
        print("网络请求错误!")
        return
    global num
    resp = json.loads(r.text)
    if resp.get('Code') == 1000:
        os.remove(wx_file_path)
        print("上传成功!")
        num = 0
    elif resp.get('Code') == 1001:
        os.remove(wx_file_path)
        print("文件已经存在!")
    else:
        if num < 10 :
            check_submit()
            num += 1
        else:
            num=0
            print("文件上传失败! 尝试10 次都未成功")

if __name__ == "__main__":
    if os.path.exists(wx_file_path) :
        check_submit()
    else:
        print("没有wx.dat 文件")