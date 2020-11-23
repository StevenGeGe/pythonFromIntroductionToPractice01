#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/23 20:44
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : pizza.py
# @Software: PyCharm


def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) + "-用以下配料将披萨英寸:")
    for topping in toppings:
        print("- " + topping)
