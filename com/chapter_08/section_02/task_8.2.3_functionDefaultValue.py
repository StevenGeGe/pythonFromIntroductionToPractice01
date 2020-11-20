#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/20 20:44
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_8.2.3_functionDefaultValue.py
# @Software: PyCharm

# 函数中，参数的默认值
# 编写函数时，可给每个形参指定默认值。
# 在调用函数中给形参提供了实参时，Python将使用指定的实参值；否则，将使用形参的默认值。

# 使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。
# 这让Python依然能够正确地解读位置实参。


def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    '''默认宠物类型：狗'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name='willie')
