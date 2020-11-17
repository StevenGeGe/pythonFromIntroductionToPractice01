#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/17 20:15
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_6.2.2_dictionaryAdd.py
# @Software: PyCharm

# 字典的使用，添加
# 字典是一种动态结构，可随时在其中添加键—值对。
# 要添加键—值对，可依次指定字典名、用方括号括起的键和相关联的值。
# Python不关心键—值对 的添加顺序，而只关心键和值之间的关联关系。

alien_0 = {'color': 'green', 'point': '5'}
print('初始字典:', end="")
print(alien_0)

# 字典添加新值
alien_0['x_point'] = 0
alien_0['y_point'] = 25
print('添加后字典:', end="")
print(alien_0)

# 对空字典进行操作，添加键值对
alien_1 = {}
alien_1['color'] = 'green'
alien_1['point'] = 5
print(alien_1)
# 输出： {'color': 'green', 'point': 5}
