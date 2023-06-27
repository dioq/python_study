# -*- coding: utf-8 -*-

# 以16进制打印 list
def list_to_hex_string(list_data):
    list_str = '['
    for i in range(0, len(list_data)):
        list_str += '0x{:02X}'.format(list_data[i])
        if i < (len(list_data) - 1):
            list_str += ","
    list_str += ']'
    return list_str


# string转bytes
def str_2_bytes():
    test_str = "abcdef"
    # 字符串转成 byte数组
    test_bytes = bytes(test_str, encoding="utf8")
    for item in test_bytes:
        print(item)


# bytes转string
def bytes_2_str():
    test_str = "abcdef"
    test_bytes = bytes(test_str, encoding="utf8")
    # byte数组 转字符串
    new_test_str = str(test_bytes, encoding='utf-8')
    print(new_test_str)


# list 使用
def list_study():
    # 定义一个list
    l1 = []
    for i in range(0, 10):
        # 在尾部追加
        l1.append(i * 10)
    l1_str = list_to_hex_string(l1)
    print(l1_str)

    l2 = [0x61, 0x62, 0x63, 0x64, 0x65, 0x66]
    # 2个list合并
    l3 = l1 + l2
    print(list_to_hex_string(l3))


# bytes 转 list
def bytes_2_list():
    test_str = "abcdef"
    test_bytes = bytes(test_str, encoding="utf8")
    l1 = list(test_bytes)
    print(list_to_hex_string(l1))


# list 转 bytes
def list_2_bytes():
    lt = [0x61, 0x62, 0x63, 0x64, 0x65, 0x66]
    my_bytes = bytes(lt)
    print(my_bytes)


if __name__ == '__main__':
    str_2_bytes()
    bytes_2_str()
    list_study()
    # bytes_2_list()
    # list_2_bytes()
