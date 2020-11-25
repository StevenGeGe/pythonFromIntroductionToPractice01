#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/25 20:22
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : car_most.py
# @Software: PyCharm


class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make  # 制造商
        self.model = model  # 型号
        self.year = year  # 年份
        self.odometer_reading = 0  # 里程表
        print("父类1构建完毕！")

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("这车有 " + str(self.odometer_reading) + " 公里.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值,拒绝将里程表往回拨"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("里程表是不能倒转的!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles


class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=60):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
        print("父类2构建完毕！")

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("这辆车还有 " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条描述电瓶续航里程的消息"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            message = "这辆车大约能走 " + str(range)
            message += " 充满电行驶里程."
            print(message)


class ElectricCar(Car):
    """模拟电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """ 初始化父类的属性，再初始化电动汽车特有的属性 """
        super().__init__(make, model, year)
        self.battery = Battery()
