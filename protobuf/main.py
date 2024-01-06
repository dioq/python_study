#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import person_pb2


def show_binary_by_hex(data):
    lt = list(data)
    for i in range(0, len(lt)):
        item = '{:02X} '.format(lt[i])
        print(item, end="")
        if (i + 1) % 0x10 == 0:
            print("")
    print("")


def test():
    # 创建一个Person对象并设置字段值
    person = person_pb2.Person()
    person.name = "张三"
    person.age = 0x20
    person.email = "zhendong2011@live.cn"

    # 序列化Person对象为二进制数据
    serialized_person = person.SerializeToString()
    # print(type(serialized_person))
    print("序列化后的数据:")
    show_binary_by_hex(serialized_person)

    # 反序列化二进制数据为一个新的Person对象
    new_person = person_pb2.Person()
    new_person.ParseFromString(serialized_person)

    # 输出新的Person对象的字段值
    print(f"反序列化后的数据：姓名={new_person.name}, 年龄={new_person.age}, 邮箱={new_person.email}")


if __name__ == '__main__':
    test()
