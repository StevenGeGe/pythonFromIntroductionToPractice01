#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/8 15:18
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_2.3.2_stringConcatenation.py
# @Software: PyCharm


# 字符串拼接
# python3 中，可以直接使用 “+” 加号来拼接字符串。
# !表示反转逻辑表达式的值

first_name = "ge"
last_name = "jin yong"
full_name = first_name + " " + last_name
print(full_name)  # 输出 ：ge jin yong

meseage = "Hello," + full_name.title() + "！"
print(meseage)  # 输出：Hello,Ge Jin Yong！
