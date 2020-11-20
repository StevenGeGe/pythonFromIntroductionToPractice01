#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/20 20:19
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_8.2.1_functionArguments.py
# @Software: PyCharm

# 传递实参
# 鉴于函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。
# 向函数传递实参的方式很多，可使用位置实参，这要求实参的顺序与形参的顺序相同；
# 也可使用关键关 字实参 字 ，其中每个实参都由变量名和值组成；还可使用列表和字典。

# 位置实参
# 调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。
# 最简单的关联方式是基于实参的顺序。这种关联方式被称为位置实参 位 。

# 在函数中，可根据需要使用任意数量的位置实参，Python将按顺序将函数调用中的实参关联到函数定义中相应的形参。

# 位置实参的顺序很重要


def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\n我有一个 " + animal_type + ".")
    print("我 " + animal_type + " 的名字叫 " + pet_name.title() + ".")


describe_pet('仓鼠', '哈利')
describe_pet('狗', '豆豆')


# 位置实参的顺序很重要


def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('哈利', '仓鼠')
