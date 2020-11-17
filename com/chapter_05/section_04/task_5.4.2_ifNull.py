#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/17 18:34
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_5.4.2_ifNull.py
# @Software: PyCharm

# 为空判断
# 判断列表是否为空
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
# 输出： Are you sure you want a plain pizza?
