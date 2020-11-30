#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/30 20:12
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_11.1.1_testFunction.py
# @Software: PyCharm

# 测试函数
# unittest模块
# formatted_name(): 需要加括号， 不然会报错。

from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: ", formatted_name(), ' .')
