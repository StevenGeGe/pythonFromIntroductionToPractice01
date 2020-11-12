#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/12 20:34
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_4.5.1_tuples.py
# @Software: PyCharm

# 元组

# 列表可以修改
# python将不能修改的值称为不可变的， 而不可变的列表称为元组。
# 元组使用圆括号'()'，来标识
# 可以通过索引访问元组，跟列表类似。

# 修改元组变量，间接的修改元组内容

# 相比于列表，元组是更简单的数据结构。
# 如果需要存储的一组值，在程序的整个生命周期内部不变，可以使用元组


dimensions = (200, 50, 100, 20)
print(dimensions[0])
print(dimensions[1])

# 修改元组内容
# 会报错
# dimensions[1] = 100
# print(dimensions)

# 循环打印元组内容
for dimension in dimensions:
    print(dimension)

# 修改元组变量
dimensions_2 = (50, 100, 20)
print(dimensions_2)
dimensions_2 = (100, 1)
print(dimensions_2)
