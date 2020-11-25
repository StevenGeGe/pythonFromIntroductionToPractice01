#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/25 20:20
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_9.4.2_mostClass.py
# @Software: PyCharm

# 在一个模块中存储多个类
# 可根据需要在一个模块中存储任意数量的类， 但尽量同一个模块中的类之间应存在某种相关性。

from car_most import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
# 输出：
# 父类1构建完毕！
# 父类2构建完毕！
# 2016 Tesla Model S
# 这辆车还有 60-kWh battery.
