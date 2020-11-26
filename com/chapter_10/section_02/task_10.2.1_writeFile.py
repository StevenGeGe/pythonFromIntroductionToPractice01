#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/26 19:16
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_10.2.1_writeFile.py
# @Software: PyCharm

# 写入文件
# open()：
#   1、参数 ：
#       1、文件名称，或者是文件路径
#       2、文件打开模式，如果不输入打开模式，默认只读模式
#           r: 读取模式
#           w: 写入模式
#           a: 附加模式
#           r+: 读取和写入模式
#       3、如果写入的文件不存在，会自动创建。
#          如果写入的文件存在，则清空并返回文件对象。
#   2、python只能将字符串写入文本文件。
#      如果要将数据存储到文本文件中，必须先使用函数str()将其转换为字符串格式
file_name = 'programming.txt'

with open(file_name, 'w') as file_object:
    file_object.write('i love xiKa')
