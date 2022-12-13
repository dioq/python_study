#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlite3


def insert():
    conn = sqlite3.connect("my.db")  # 连接数据库
    c = conn.cursor()
    print("数据库打开成功")

    sql = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Paul', 33, 'California', 20000.00 );"
    c.execute(sql)

    conn.commit()  # 执行sql语句
    print("数据插入成功")
    conn.close()  # 关闭数据库连接


def query():
    conn = sqlite3.connect("my.db")  # 连接数据库
    c = conn.cursor()
    print("数据库打开成功")

    sql = "SELECT id, name, address, salary  from COMPANY;"
    cursor = c.execute(sql)
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")

    print("数据操作成功")
    conn.close()  # 关闭数据库连接


if __name__ == '__main__':
    insert()
    query()
