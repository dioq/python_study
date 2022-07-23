import os
import sys


def testFunc():
    print("file path : ", __file__)
    print("文件名 :", os.path.basename(__file__))
    print("函数名 :", __name__)
    print("行号   :", sys._getframe().f_lineno)


if __name__ == "__main__":
    testFunc()
