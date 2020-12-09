#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/12/9 20:12
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_16-1-1_csv.py
# @Software: PyCharm

# 1、模块csv 包含函数next() ，调用它并将阅读器对象传递给它时，它将返回文件中的下一行。
#   在前面的代码中，
#   只调用了next() 一次，因此得到的是文件的第一行，其中 包含文件头
# 2、文件头的格式并非总是一致的，空格和单位可能出现在奇怪的地方。


import csv

file_name = 'data/sitka_weather_07-2018_simple.csv'

with open(file_name) as file_object:
    reader = csv.reader(file_object)
    # 打印文件头
    header_row = next(reader)
    print(header_row)
    # 输出： ['STATION', 'NAME', 'DATE', 'PRCP', 'TAVG', 'TMAX', 'TMIN']

    # 打印文件头，及其位置
    for index, column_header in enumerate(header_row):
        print(index, column_header)
        # 输出：
        # 0 STATION
        # 1 NAME
        # 2 DATE
