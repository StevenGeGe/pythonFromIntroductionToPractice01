#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/12/8 10:24
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_15-1-1_matplotlib.py
# @Software: PyCharm

# 1、数据可视化 指的是通过可视化表示来探索数据，它与数据挖掘紧密相关，
#       而数据挖掘指的是使用代码来探索数据集的规律和关联。
# 2、数据集可以是用一行代码就能表 示的小型数字列表，也可以是数以吉字节的数据。
# 3、matplotlib，它是一个数学绘图库，我们将使用它来制作简单的图表，如折线图和散点图。
# 4、Pygal, 专注于生成适合在数字设备上显示的图表。通过使用Pygal，可在用户与图表交互时突出元素以及调整其大小，还可轻松地调整整个图表的尺 寸，
#       使其适合在微型智能手表或巨型显示器上显示。
# 5、http://matplotlib.org/， 图表详解官网。

# 6、模块pyplot 包含很多用于生成图表的函数
# 7、创建了一个列表，在其中存储前述平方数，再将这个列表传递给函数plot() ，这个函数尝试根据这些数字绘制出有意义的图形。
# 8、plt.show() 打开matplotlib查看器，并 显示绘制的图形。
# 9、查看器让你能够缩放和导航图形，另外，单击磁盘图标可将图形保存起来。

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

plt.plot(squares)
plt.show()
