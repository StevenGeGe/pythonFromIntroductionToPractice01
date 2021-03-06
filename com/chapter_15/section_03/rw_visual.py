#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/12/8 21:03
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : rw_visual.py
# @Software: PyCharm


# 函数figure() 用于指定图表的宽度、高度、分辨率和背景色。
#   形参figsize 指定一个元组，向matplotlib指出绘图窗口的尺寸，单位为英寸。

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    # dpi: 系统的分辨率
    plt.figure(dpi=128, figsize=(20, 16))

    point_numbers = list(range(rw.num_points))
    # 使用颜色映射来指出漫步中各点的先后顺序，并删除每个点的黑色轮廓，让它们的颜色更明显.
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                cmap=plt.cm.Blues, edgecolors='none', s=1)
    # 重新绘制起点和终点，并突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴， 会报出警告
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk？(y/n)")
    if keep_running == 'n' or keep_running == 'N':
        break
