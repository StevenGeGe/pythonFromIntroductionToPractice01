#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/11 21:52
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_4.3.4_listAnalytical.py
# @Software: PyCharm

# 列表解析
# 这里的for循环没有冒号。
# 简化创建操作
# value ** 2: 是一个表达式
# value : 是一个寻常的中间值
# for ： for循环，但是for循环后面没有冒号。
# range(1, 11): 取值函数

squares = [value ** 2 for value in range(1, 11)]
print(squares)  # 输出：[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
