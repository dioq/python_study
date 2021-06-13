import time
import win32api
import win32con

# win32api.keybd_event
# 该函数原型：keybd_event(bVk, bScan, dwFlags, dwExtraInfo)
#       第一个参数：虚拟键码（键盘键码对照表见附录）；
#       第二个参数：硬件扫描码，一般设置为0即可；
#       第三个参数：函数操作的一个标志位，如果值为KEYEVENTF_EXTENDEDKEY则该键被按下，也可设置为0即可，如果值为KEYEVENTF_KEYUP则该按键被释放；
#       第四个参数：定义与击键相关的附加的32位值，一般设置为0即可。

win32api.keybd_event(13, 0, 0, 0)  # enter
win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
# 按下ctrl+s
win32api.keybd_event(0x11, 0, 0, 0)
win32api.keybd_event(0x53, 0, 0, 0)
win32api.keybd_event(0x53, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(1)
# 按下回车
win32api.keybd_event(0x0D, 0, 0, 0)
win32api.keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(1)
# 按下ctrl+W
win32api.keybd_event(0x11, 0, 0, 0)
win32api.keybd_event(0x57, 0, 0, 0)
win32api.keybd_event(0x57, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
# 按下ctrl+a
win32api.keybd_event(0x11, 0, 0, 0)
win32api.keybd_event(0x41, 0, 0, 0)
win32api.keybd_event(0x41, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(1)
# 按下ctrl+v
win32api.keybd_event(0x11, 0, 0, 0)
win32api.keybd_event(0x56, 0, 0, 0)
win32api.keybd_event(0x56, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(1)
