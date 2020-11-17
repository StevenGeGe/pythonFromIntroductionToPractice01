#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/17 18:24
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_5.4.1_if.py
# @Software: PyCharm

# for检查所有元素
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

# for - if 检查特殊元素
requested_toppings_2 = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping_2 in requested_toppings_2:
    if requested_topping_2 == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping_2 + ".")
print('Finished making your pizza!')
