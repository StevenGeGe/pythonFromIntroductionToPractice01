#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/12/9 16:21
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : die_visual.py
# @Software: PyCharm

from die import Die

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

print(frequencies)
