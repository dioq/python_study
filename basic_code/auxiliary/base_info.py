#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys


def testFunc():
    print("file path : ", __file__)
    print("file name :", os.path.basename(__file__))
    print("function name :", sys._getframe().f_code.co_name)
    print("line :", sys._getframe().f_lineno)


if __name__ == "__main__":
    testFunc()
