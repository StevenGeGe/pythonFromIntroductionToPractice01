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

# 创建一个D6
die = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果可视化
hist = pygal.Bar()

hist.title = "滚动一个D6 1000次的结果"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist._x_title = "结果"
hist._y_title = "频率结果"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
# 查看生成的地址， 浏览器访问 ：
#   file:///F:/data/workspace_data/python_data/pythonFromIntroductionToPractice01/com/chapter_15/section_04/die_visual.svg
