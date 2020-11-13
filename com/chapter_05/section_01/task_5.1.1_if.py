#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/13 17:07
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_5.1.1_if.py
# @Software: PyCharm

# if: 判断
# 格式：
#      if 判断表达式:
#         print(条件为真，打印)
#     else:
#         print(条件为假，打印)

# str.upper(): 字符串全部大写：
# str.title(): 字符串首字母大写

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper() + '\t', end='')
    else:
        print(car.title() + '\t', end='')
