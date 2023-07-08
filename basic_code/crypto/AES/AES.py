#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from Crypto.Cipher import AES

"""
pip3 install pycryptodome
"""
import base64


class Crypto:
    def __init__(self, key, iv):
        self.key = key.encode('utf-8')
        self.iv = iv.encode('utf-8')

    # @staticmethod
    def add_pkcs7padding(self, data: bytes):
        """明文使用PKCS7填充 """
        bs = 16
        padding_size = bs - (len(data) % bs)
        padding_list = []
        for i in range(0, padding_size):
            padding_list.append(padding_size)

        # print("padding_size:{}\n{}".format(padding_size,padding_list))
        data_list = list(data)
        new_list = data_list + padding_list
        # print("new_list:{}\n".format(list_to_hex_string(new_list)))
        data_bytes = bytes(new_list)
        return data_bytes

    def remove_pkcs7padding(self, data: bytes):
        data_len = len(data)
        padding_size = data[data_len - 1]
        # print("padding_size1:{}".format(padding_size))

        repeat_num = 0
        for i in range(data_len - 16, data_len):
            num = data[i]
            # print("{index}-->{value}".format(index=i, value=num))
            if num == padding_size:
                repeat_num += 1

        # print("num_size:",num_size)
        if repeat_num != padding_size:
            padding_size = 0

        # print("padding_size:", padding_size)
        real_size = data_len - padding_size
        return data[:real_size]

    def aes_encrypt(self, content):
        """ AES加密 """
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        # 处理明文
        content_with_padding = self.add_pkcs7padding(content)
        # 加密
        encrypt_bytes = cipher.encrypt(content_with_padding)
        return encrypt_bytes

    def aes_decrypt(self, content):
        """AES解密 """
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        # print("content:{}\n".format(list_to_hex_string(list(content))))
        plaintext_bytes = cipher.decrypt(content)
        plaintext_bytes_without_padding = self.remove_pkcs7padding(plaintext_bytes)

        return plaintext_bytes_without_padding


def list_to_hex_string(list_data):
    list_str = '['
    for i in range(0, len(list_data)):
        list_str += '0x{:02X}'.format(list_data[i])
        if i < (len(list_data) - 1):
            list_str += ","
    list_str += ']'
    return list_str


if __name__ == '__main__':
    key = 'ONxYDyNaCoyTzsp83JoQ3YYuMPHxk3j7'
    iv = 'yNaCoyTzsp83JoQ3'

    plaintext = "Put setup code here."
    plaintext_bytes = bytes(plaintext, encoding="utf8")

    crypto = Crypto(key=key, iv=iv)
    ciphertext_bytes = crypto.aes_encrypt(plaintext_bytes)
    print(list_to_hex_string(list(ciphertext_bytes)))
    print(len(ciphertext_bytes))
    ciphertext_base64 = str(base64.b64encode(ciphertext_bytes), encoding='utf-8')
    print("ciphertext:", ciphertext_base64)

    plaintext2 = crypto.aes_decrypt(ciphertext_bytes)
    plaintext2_base64 = str(plaintext2, encoding='utf-8')
    print("plaintext:", plaintext2_base64)
