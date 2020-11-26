#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/26 19:31
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_10.2.2_writeMostLine.py
# @Software: PyCharm

# 向文件中写入多行
# write(): 函数不会在文本末尾添加换行符。

file_name = 'programming.txt'

with open(file_name, 'w') as file_object:
    file_object.write('i love xiKa')
    file_object.write('i love all day')
