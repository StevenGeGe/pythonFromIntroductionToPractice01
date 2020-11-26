#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/26 10:55
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_10.1.1_readFile.py
# @Software: PyCharm

# 读取文件
# open() : 打开一个文件，
#   参数：
#       1、传入打开文件的名称，
#       2、传入文件的路径和名称， 注意，Windows(反斜杠\)和linux(斜杠/)中的路径表示方法不同
#       3、传入的路径可以是相对路径，也可以是绝对路径
#   查找路径：默认在当前目录查找该文件。
#   返回： 返回一个表示该文件的对象。
# with： 在不需要访问文件后，python自动将其关闭。
# file_object.read(): 读取文件中全部内容
# file_object.read().rstrip()：删除字符串末尾多余的空行

import time

time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(time_str + "\n" + contents.rstrip())
# 输出：
# 2020-11-26 17:38:43
# 3.1415926535
# 8979323846
# 2643383279

with open(
        'F:\data\workspace_data\python_data\pythonFromIntroductionToPractice01\com\chapter_10\section_01\pi_digits.txt') \
        as file_object_2:
    contents_2 = file_object_2.read()
    print(time_str + "\n" + contents_2.rstrip())
# 输出： 2
# 020-11-26 17:38:43
# 3.1415926535
# 8979323846
# 2643383279
