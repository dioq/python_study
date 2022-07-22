#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import threading
import time


def show(arg,arg1):
    time.sleep(1)
    str = "thread {arg} \t {arg1}  running ....".format(arg=arg,arg1=arg1)
    print(str)


if __name__ == '__main__':
    for i in range(9):
        start_time = time.time()
        t = threading.Thread(target=show, args=(i,start_time,))
        t.start()
