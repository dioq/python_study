# -*- coding:utf8 -*-
import wda
import time

# for debug
# Enable debug will see http Request and Response
# wda.DEBUG = True

wda.DEBUG = False # default False
wda.HTTP_TIMEOUT = 180.0 # default 180 seconds
wda.DEVICE_WAIT_TIMEOUT = 180.0

d = wda.USBClient("58dad54ccf463a7cf3752365408d766808f40ffd", port=8100) # 指定设备 udid 和WDA 端口号
# c = wda.USBClient("9a74558f8e341d056731d9c8aa532107c48cb65c", port=8100) # 指定设备 udid 和WDA 端口号


d.home()
d(label="设置").click()
d(label="通用", name="通用").click()

d(label="传输或还原iPhone", name="传输或还原iPhone").click()
d(label="抹掉所有内容和设置", name="抹掉所有内容和设置").click()
d.xpath('//Window[1]/Other[2]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Button[1]').click()
d.xpath('//Sheet/Other[1]/Other[1]/Other[2]/ScrollView[2]').click()