#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/25 18:36
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_9.3.5_InstanceAttributes.py
# @Software: PyCharm

# 实例属性
# 模拟实物时，如果类添加的细节过多，属性和方法清单以及文件都会很长，
# 在这种情况下，可以将类的一部分独立出来作为一个独立的小类。


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


class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
        print("父类2构建完毕！")

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("这辆车还有 " + str(self.battery_size) + "-kWh 电量.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "这辆车大约能走 " + str(range)
        message += " 充满电行驶里程."
        print(message)


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性， 再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()  # 电瓶容量 # 构建ElectricCar时，会自动创建一个Battery实例
        print("子类1构建完毕！")

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("这辆车有 " + str(self.battery_size) + "-kWh 电量.")


my_tesla = ElectricCar('特斯拉', 'model s', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
# 输出：
# 父类构建完毕！
# 父类2构建完毕！
# 子类1构建完毕！
# 2020 特斯拉 Model S
# 这辆车还有 70-kWh 电量.
my_tesla.battery.get_range()
# 输出： 这辆车大约能走 240 充满电行驶里程.
