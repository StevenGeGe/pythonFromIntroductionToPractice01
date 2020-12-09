#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/12/9 20:36
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_16-1-3_extractData.py
# @Software: PyCharm

# 提取文件并读取数据

import csv

# 从文件中获取最高温

file_name = 'data/sitka_weather_07-2018_simple.csv'

with open(file_name) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    highs = []
    # 按行读取， 然后选取每行的第六个元素
    for row in reader:
        highs.append(row[5])
    print(highs)
