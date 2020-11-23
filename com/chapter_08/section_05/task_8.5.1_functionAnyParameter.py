#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/23 19:54
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_8.5.1_functionAnyParameter.py
# @Software: PyCharm

# 向函数内传递任意参数
# def function(*parammeter_name):
# *parammeter_name: 为空的元组
# Python将实参封装到一个元组中，即便函数只收到一个值也如此

# 接受不同类型的参数
# 如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。
# Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。

def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 输出：
# ('pepperoni',)
# ('mushrooms', 'green peppers', 'extra cheese')


def make_pizza(*toppings):
    """概述要制作的比萨"""
    print("\n用下列配料制作披萨:")
    for topping in toppings:
        print("- " + topping)


make_pizza('pepperoni')
# 输出：
# 用下列配料制作披萨:
# - pepperoni
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# 输出：
# 用下列配料制作披萨:
# - mushrooms
# - green peppers
# - extra cheese

# --------------------------------------------------
print("接受不同类型参数：")


def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) + "-用以下配料将披萨英寸:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
