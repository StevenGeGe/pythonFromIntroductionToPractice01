#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/20 20:34
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_8.2.2_functionKeywordArguments.py
# @Software: PyCharm


# 函数中的关键字实参

# 关键字实参 是传递给函数的名称—值对。
# 使用关键字实参时，务必准确地指定函数定义中的形参名。

def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\n我有一个 " + animal_type + ".")
    print("我的 " + animal_type + "的名字叫 " + pet_name.title() + ".")


describe_pet(animal_type='仓鼠', pet_name='哈利')
