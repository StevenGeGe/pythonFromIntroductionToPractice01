#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/12/8 14:40
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_15-1-3_ scatter.py
# @Software: PyCharm

# scatter(): 绘制散点图并设置样式
# 传递一对，x和y坐标，它将在指定位置绘制一个点。


import matplotlib.pyplot as plt

# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.scatter(2, 4, s=200)

# 设置图表标题
plt.title("平方数散点图", fontsize=24)

# 给坐标轴加上标签
plt.xlabel("数值", fontsize=14)
plt.ylabel("平方", fontsize=14)

# 设置刻度标记大小
plt.tick_params(axis="both", which="major", labelsize=14)

# 散点图表展示
plt.show()
