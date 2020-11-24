#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/24 15:29
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_8.6.3_as.py
# @Software: PyCharm

#  使用 as给函数指定别名
# 如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，
# 可指定简短而独一无二的别名别 ——函数的另一个名称，类似于外号

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
