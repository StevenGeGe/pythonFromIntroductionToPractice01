#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/25 20:10
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_9.4.1_importClass.py
# @Software: PyCharm

# python3 允许将类存储在模块中，然后在主程序中导入所需的模块
# 导入类是一种有效的编程方式。
# ！通过将这个类移到一个模块中，并导入该模块，你依然可以使用其所有功能，但主程序文 件变得整洁而易于阅读.

from car import Car

my_new_car = Car('audi', 'a6', 2020)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
