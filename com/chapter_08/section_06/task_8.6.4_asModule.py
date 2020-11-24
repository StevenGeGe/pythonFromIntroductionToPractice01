#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/24 15:33
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_8.6.4_asModule.py
# @Software: PyCharm

# 给模块起别名
#  可以给模块指定别名。
# 通过给模块指定简短的别名（如给模块pizza 指定别名p ），让你能够更轻松地调用模块中的函数

import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
