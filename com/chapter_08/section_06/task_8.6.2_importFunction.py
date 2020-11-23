#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/23 20:58
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_8.6.2_importFunction.py
# @Software: PyCharm

# 导入特定的函数

# 样式： from module_name import function_name
# 通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数：
# 样式：from module_name import function_0, function_1, function_2

from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
