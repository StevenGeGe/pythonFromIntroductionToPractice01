#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/24 20:01
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_9.2.1_classUse.py
# @Software: PyCharm

# 类的使用


class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make  # 制造商
        self.model = model  # 型号
        self.year = year  # 年份

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


my_new_car = Car('奥迪', 'a6', 2020)
print(my_new_car.get_descriptive_name())
