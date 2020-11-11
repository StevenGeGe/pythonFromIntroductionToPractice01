#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/11 11:47
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_4.3.1_range.py
# @Software: PyCharm

# 数值列表

# 生成一系列的数字
# range():
# 如果使用ranges(),输出结果不符合预期，可以尝试将指定值加1或减1
# 可以将range()，创建的数字直接赋值给列表。
# 可以指定步长,(其前面一项 减去  后面一项 等于2)

# **： 表示乘方运算

for values in range(1, 5):
    print(values, end="")
# 输出： 1 2 3 4
print()

# 直接赋值给列表
number = list(range(1, 11))
print(number)  # 输出: [1, 2, 3, 4]

# 指定步长
event_number = list(range(2, 11, 2))
print(event_number)  # 输出:  [2, 4, 6, 8, 10]

# 将乘方运算赋值给列表
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)  # 输出： [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 优化版
squares_2 = []
for value_2 in range(1, 11):
    squares_2.append(value_2 ** 2)
print(squares_2)  # 输出： [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
