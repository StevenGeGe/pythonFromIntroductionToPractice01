#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/12/8 14:40
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_15-1-3_ scatter.py
# @Software: PyCharm

# scatter(): 绘制散点图并设置样式
# 传递一对，x和y坐标，它将在指定位置绘制一个点。

# 绘制一系列的点， 只需要传递两个包含x和y值的列表。


import matplotlib.pyplot as plt

# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 单个散点
# plt.scatter(2, 4, s=200)
# 多个散点
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# 自动计算数据
x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]
plt.scatter(x_values, y_values, s=200)

# 设置图表标题
plt.title("平方数散点图", fontsize=24)

# 给坐标轴加上标签
plt.xlabel("数值", fontsize=14)
plt.ylabel("平方", fontsize=14)

# 设置刻度标记大小
plt.tick_params(axis="both", which="major", labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# 散点图表展示
plt.show()
