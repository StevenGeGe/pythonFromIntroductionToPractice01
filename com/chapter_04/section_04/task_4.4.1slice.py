#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/12 19:39
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_4.4.1slice.py
# @Software: PyCharm

# 列表中的切片
# 切片： 对于列表中的元素，切开处理。
# 根据列表中的索引进行分割。

# 指定开始，结束索引
players = ['a', 'b', 'c', 'd', 'e']
print(players[0:2])

# 指定结尾索引
# 如果只指定结尾索引，没有指定起始索引，则默认从头开始
print(players[:3])

# 指定起始索引
# 如果只指定起始索引，则默认到列表的结尾结束
print(players[2:])
