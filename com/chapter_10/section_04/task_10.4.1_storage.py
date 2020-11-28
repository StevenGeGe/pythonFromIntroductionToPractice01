#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/28 21:23
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_10.4.1_storage.py
# @Software: PyCharm

# 存储数据
# JSON（JavaScript Object Notation）格式最初是为JavaScript开发的，但随后成了一种常见格式，
#   被包括Python在内的众多语言采用。
# json.dump() 接受两个实参：要存储的数据以及可用于存储数据的文件对象
# json.dumps(): 对数据进行编码。
#   1、json_object - > string
#   2、写入json文件。
# json.loads(): 对数据进行解码。
#   1、string -> json_object
#   2、从json文件读取数据。

import json

numbers = [2, 3, 5, 7, 11, 13]

file_name = 'numbers.json'

# 将数据存储到json文件中
with open(file_name, 'w') as file_object_write:
    json.dump(numbers, file_object_write)

# 从json文件中读取数据
with open(file_name, 'r') as file_object_read:
    numbers_2 = json.load(file_object_read)
print("number_2 : ", numbers_2)
# 输出： number_2 :  [2, 3, 5, 7, 11, 13]
