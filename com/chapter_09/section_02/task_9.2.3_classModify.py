#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/24 20:14
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_9.2.3_classModify.py
# @Software: PyCharm

# 类中属性的修改
# 三种方式修改属性的值：
#   1、直接通过实例进行修改；
#   2、通过方法进行设置；
#   3、通过方法进行递增（增加特定的值）


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

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles


# 直接修改属性的值
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# 输出：
# 2016 Audi A4
# 这车有 23 公里.


# 通过方法修改属性的值
my_new_car.update_odometer(26)
my_new_car.read_odometer()
# 输出： 这车有 26 公里.


# 通过方法对属性的值进行递增
my_used_car = Car('subaru', 'outback', 2013)
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
