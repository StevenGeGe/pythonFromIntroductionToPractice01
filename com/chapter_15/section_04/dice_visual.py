#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/12/9 16:21
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : die_visual.py
# @Software: PyCharm

# 直方图是一种条形图，指出了各种结果出现的频率。

from die import Die
import pygal

# 创建两个D6骰子
die_1 = Die()
die_2 = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果可视化
hist = pygal.Bar()

hist.title = "滚动两个个D6 1000次的结果"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist._x_title = "结果"
hist._y_title = "频率结果"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
# 查看生成的地址， 浏览器访问 ：
#   file:///F:/data/workspace_data/python_data/pythonFromIntroductionToPractice01/com/chapter_15/section_04/die_visual.svg
