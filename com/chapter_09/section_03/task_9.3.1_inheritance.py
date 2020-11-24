#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/24 20:34
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_9.3.1_inheritance.py
# @Software: PyCharm

# python3中，类的继承
# 创建子类的是实例时， python3会首先需要完成给父类的所有属性赋值。
# super() 是一个特殊函数，帮助Python将父类和子类关联起来。
# 父类也称为超类超 （superclass），名称super因此而得名。


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
        """初始化父类的属性"""
        super().__init__(make, model, year)
        print("子类构建完毕！")


my_tesla = ElectricCar('特斯拉', 'model s', 2016)
print(my_tesla.get_descriptive_name())

# 输出：
# 父类构建完毕！
# 子类构建完毕！
# 2016 特斯拉 Model S
