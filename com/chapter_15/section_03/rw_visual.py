#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/12/8 21:03
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : rw_visual.py
# @Software: PyCharm

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 创建一个RandomWalk实例，并将其包含的点都绘制出
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
