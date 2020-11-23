#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/23 20:42
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_8.6.1.1_moduleUse.py
# @Software: PyCharm

# 使用创建的模块
# 虽然会提示找不到该模块，但如果默认在同级目录下，也会运行成功
import pizza

pizza.make_pizza(18, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
