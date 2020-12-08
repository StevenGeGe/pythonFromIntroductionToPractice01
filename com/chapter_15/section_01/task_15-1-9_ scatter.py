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

# 颜色映射
# 1、是一系列颜色，它们从起始颜色渐变到结束颜色。
# 2、在可视化中，颜色映射用于突出数据的规律。
#   你可能用较浅的颜色来显示较小的值，并使用较深 的颜色来显示较大的值。

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
x_values = list(range(1001))
y_values = [x ** 2 for x in x_values]

# s=10: 散点大小
# plt.scatter(x_values, y_values, s=10)
# edgecolor='none': 删除数据点的轮廓
# plt.scatter(x_values, y_values, edgecolor='none', s=10)
# c='red' : 自定义散点的颜色
# plt.scatter(x_values, y_values, c='red', edgecolor='none', s=10)
# c=(0, 0, 0.8)： 使用RGB颜色模式，自定义颜色。
# 值越接近0，指定的颜色越深，值越接近1，指定的颜色越浅。
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)
# 颜色映射
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

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
