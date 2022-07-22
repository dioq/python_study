# -*- coding: utf-8 -*-

#uuid="fafafafaf"
# print("失败手机的uuid:",uuid)

# tryTimes = 1
# print("上传62数据,尝试第", tryTimes, "次")

resp="8ca333c7df73fd84c9b5c1fc2ec914875c6ff976----"
respArr = resp.split("----")
print(len(respArr))
print(respArr[0])
print(respArr[1])
if len(respArr) == 2 or respArr[1] == "":
    # cleanDevice(uuid)
    print("go here")
