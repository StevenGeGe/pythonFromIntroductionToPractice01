#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/24 20:48
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_9.3.3_subclassFunction.py
# @Software: PyCharm

# 在python3中，给子类定义属性方法


class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make  # 制造商
        self.model = model  # 型号
        self.year = year  # 年份
        self.odometer_reading = 0  # 里程表
        print("父类构建完毕！")

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


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性， 再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery_size = 70  # 电瓶容量
        print("子类构建完毕！")

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("这辆车有 " + str(self.battery_size) + "-kWh 电量.")


my_tesla = ElectricCar('特斯拉', 'model s', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
# 输出：
# 父类构建完毕！
# 子类构建完毕！
# 2020 特斯拉 Model S
# 这辆车有 70-kWh 电量.
