#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import uuid


def random_uuid():
    uid = uuid.uuid1()
    uid = str(uid).upper()
    print(uid)


if __name__ == '__main__':
    random_uuid()
