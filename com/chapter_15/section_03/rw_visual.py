#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/12/8 21:03
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : rw_visual.py
# @Software: PyCharm

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    # 使用颜色映射来指出漫步中各点的先后顺序，并删除每个点的黑色轮廓，让它们的颜色更明显.
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                cmap=plt.cm.Blues, edgecolors='none', s=15)
    plt.show()

    keep_running = input("Make another walk？(y/n)")
    if keep_running == 'n' or keep_running == 'N':
        break
