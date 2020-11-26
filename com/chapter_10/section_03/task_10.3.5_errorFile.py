#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/26 20:32
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_10.3.5_errorFile.py
# @Software: PyCharm

# 处理文件异常

file_name = 'alice.txt'
# 会因找不到文件而报错
# with open(file_name) as file_object:
#     contents = file_object.read()

try:
    with open(file_name) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("抱歉 ", file_name, "这个文件不存在")
# 输出： 抱歉  alice.txt 这个文件不存在
