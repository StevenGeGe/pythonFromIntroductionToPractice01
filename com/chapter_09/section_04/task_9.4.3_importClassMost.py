#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/25 20:27
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_9.4.3_importClassMost.py
# @Software: PyCharm

# 从一个模块中导入多个类
from car_most import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
# 输出：
# 父类1构建完毕！
# 2016 Volkswagen Beetle
# 父类1构建完毕！
# 父类2构建完毕！
# 2016 Tesla Roadster
