#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/12/24 21:03
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_16-1-7_csvDateMoreTime.py
# @Software: PyCharm

# 涵盖更长的时间

import csv
from datetime import datetime
from matplotlib import pyplot as plt

# 从文件中获取最高温

file_name = 'data/sitka_weather_2018_full.csv'

# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

with open(file_name) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    dates, highs = [], []
    # 按行读取， 然后选取每行的第六个元素
    for row in reader:
        # 接收时间
        current_date = datetime.strptime(row[2], "%Y/%m/%d")
        dates.append(current_date)
        # 转换成数字
        tmp = float(row[3])
        high = int(tmp)
        highs.append(high)
    print(highs)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c="red")

# 设置图形格式
plt.title("2018年七月每日气温", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("温度(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
