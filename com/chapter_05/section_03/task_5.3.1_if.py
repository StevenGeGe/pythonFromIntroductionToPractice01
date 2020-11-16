#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/16 10:39
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_5.3.1_if.py
# @Software: PyCharm

# if 判断操作
age = 19
if age >= 18:
    print('You are old enough to vote!')

# if else 判断操作
age_2 = 17
if age >= 18:
    print('You are old enough to vote!')
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
# 输出：You are old enough to vote!
#      Have you registered to vote yet?


# 经过超过两个的情形，可以使用if-elif-else 结构
age_3 = 12
if age_3 < 4:
    print("Your admission cost is $0.")
elif age_3 < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
# 输出： Your admission cost is $5.


# 使用多个elif代码块
age_4 = 12
if age_4 < 4:
    price = 0
elif age_4 < 18:
    price = 5
elif age_4 < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")
# 输出： Your admission cost is $5.


# 省略else代码块
# Python并不要求if-elif 结构后面必须有else 代码块。
# 在有些情况下，else 代码块很有用；
# 而在其他一些情况下，使用一条elif 语句来处理特定的情形更清晰：
age_5 = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")
# 输出： Your admission cost is $10.
