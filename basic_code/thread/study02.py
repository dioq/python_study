#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import threading
import time


def dowaiting():
    print('start waiting:', time.strftime('%H:%M:%S'))
    time.sleep(3)
    print('stop waiting', time.strftime('%H:%M:%S'))


if __name__ == '__main__':
    t = threading.Thread(target=dowaiting)
    t.start()
    # 确保线程t已经启动
    time.sleep(1)
    print('start job')
    print('end job')
