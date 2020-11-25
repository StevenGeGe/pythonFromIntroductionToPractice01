#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/25 20:12
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : car.py
# @Software: PyCharm


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
        """将里程表读数设置为指定的值,拒绝将里程表往回拨"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("里程表是不能倒转的!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles
