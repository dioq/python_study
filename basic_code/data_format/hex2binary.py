#!/usr/bin/python3
# -*- coding: UTF-8 -*-


def extra2_binary(data):
    b = bin(int(data, 16))[2:].zfill(8 * 4)
    print(b)


if __name__ == '__main__':
    extra2_binary("D2C00212")
