#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/17 18:39
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_5.4.3_ifMoreList.py
# @Software: PyCharm

# 判断多个列表

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping)
    else:
        print("Sorry, we don't have " + requested_topping)
print("\nFinished making your pizza!")
# 输出： Adding mushrooms
# Sorry, we don'thave french fries
# Adding extra cheese
#
# Finished making your pizza!

