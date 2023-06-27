# -*- coding: utf-8 -*-
import hashlib


def test_sha256():
    test_str = "abcdef"
    test_bytes = bytes(test_str, encoding="utf8")
    # print(randomSed)
    hs = hashlib.sha256(test_bytes).hexdigest()
    print(hs)


def test_md5():
    test_str = "abcdef"
    test_bytes = bytes(test_str, encoding="utf8")
    hs = hashlib.md5(test_bytes).hexdigest()
    print(hs)


if __name__ == '__main__':
    # test_sha256()
    test_md5()
