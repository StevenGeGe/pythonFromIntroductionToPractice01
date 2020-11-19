#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/19 20:36
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_7.1.3_modulus.py
# @Software: PyCharm

# 求模运算
# 求模运算符，不会指出一个数是另一个数的多少倍， 只会指出余数是多少。
# 可以利用这一点来判断是奇数还是偶数。

number = int(input("输入你的数字："))

if (number % 2) == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
