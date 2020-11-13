#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/13 17:17
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_5.2.1_ifTest.py
# @Software: PyCharm

# if条件测试
# 每条if语句的核心都是一个值为True或者False的表达式，这种表达式被称为条件测试。
# 检查是否相等
# 检查是否相等时，不考虑大小写
# 检查是否不相等
# 比较数字

# 检查条件是否相等
car = 'bmw'
print(car == 'bmw')  # 输出：True
print(car == 'audi')  # 输出：False

# 检查是否相等时，不考虑大小写
car = 'Audi'
print(car.lower() == 'audi')  # 输出： True

# 检查是否不相等
# 可结合（！=） ， 表示 不。
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# 比较数字
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

# 检查多个条件
# and
# 为了增加可读性，可以将每个测试都放在一对括号中
age_1 = 22
age_2 = 18
print(age_1 >= 21 and age_2 >= 21)  # 输出： False

age_2 = 22
print(age_1 >= 21 and age_2 >= 21)  # 输出： True
# 放在括号中
print((age_1 >= 21) and (age_2 >= 21))  # 输出： True

# or
age_3 = 22
age_4 = 18
print((age_3 >= 21) or (age_4 >= 21))  # 输出： True

age_3 = 18
print((age_3 >= 21) or (age_4 >= 21))  # 输出： False
