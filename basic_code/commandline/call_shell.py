#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


def way01Func():
    shell_file = "test.sh"
    # 无法获得cmd命令的输出
    os.system(shell_file)


if __name__ == "__main__":
    way01Func()
