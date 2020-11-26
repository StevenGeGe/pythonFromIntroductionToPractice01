#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/26 17:41
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_10.1.2_readFileLine.py
# @Software: PyCharm

# 逐行读取文件
# rstrip()： 删除空白行
# 类似于，将所有内容读取出来后，逐行打印

import time

file_name = 'pi_digits.txt'

time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

with open(file_name) as file_object:
    for line in file_object:
        print(time_str + " " + line.rstrip())
