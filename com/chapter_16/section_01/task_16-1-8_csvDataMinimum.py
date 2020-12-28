#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/12/28 20:25
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_16-1-8_csvDataMinimum.py
# @Software: PyCharm


import csv
from datetime import datetime
from matplotlib import pyplot as plt

# 从文件中获取最高温

file_name = 'data/death_valley_2018_full.csv'

# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

with open(file_name) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    # 按行读取， 然后选取每行的第六个元素
    for row in reader:
        # 接收时间
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)
        # 转换成数字
        # 异常报错，未找到原因
        # 换了数据文件正常了
        high = int(row[6])
        highs.append(high)

        low = int(row[7])
        lows.append(low)
    print(highs)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
# 没有颜色的
plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")

# 设置图形格式
plt.title("2018年七月每日气温", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("温度(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

# 有面积颜色的
plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.show()
