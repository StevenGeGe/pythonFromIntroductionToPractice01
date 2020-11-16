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
