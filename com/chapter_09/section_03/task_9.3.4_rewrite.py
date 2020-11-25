#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/25 18:21
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_9.3.4_rewrite.py
# @Software: PyCharm

# 重写父类的方法，继承
#  1、对于父类的方法，只要它不符合子类模拟的实物的行为，都可对其进行重写。
#  2、可在子类中定义一个这样的方法，即它与要重写的父类方法同名。
#    这样，Python将不会考虑这 个父类方法，而只关注你在子类中定义的相应方法。


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

    def fill_gas_tank(self):
        """汽车油箱"""
        print("汽车的油箱是20L!")


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

    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("这是电动汽车不需要油箱!")


my_car = ElectricCar('特斯拉', 'model s', 2020)
my_car.fill_gas_tank()
# 输出： 这是电动汽车不需要油箱!

my_new_car = Car('奥迪', 'a6', 2020)
my_new_car.fill_gas_tank()
# 输出： 汽车的油箱是20L!
