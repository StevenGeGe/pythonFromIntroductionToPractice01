#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/24 20:07
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_9.2.2_classInit.py
# @Software: PyCharm

# 给类中的属性指定默认值


class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make  # 制造商
        self.model = model  # 型号
        self.year = year  # 年份
        self.odometer_reading = 0  # 里程表

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("这车有 " + str(self.odometer_reading) + " 公里.")


my_new_car = Car('奥迪', 'a6', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
# 输出：
# 2016 奥迪 A6
# 这车有 0 公里.
