#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/20 20:49
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_8.2.4_functionCallUse.py
# @Software: PyCharm

# 等效的函数调用
# 鉴于可混合使用位置实参、关键字实参和默认值，通常有多种等效的函数调用方式。


def describe_pet(pet_name, animal_type='dog'):
    """
    基于这种定义，在任何情况下都必须给pet_name 提供实参；
    指定该实参时可以使用位置方式，也可以使用关键字方式。
    如果要描述的动物不是小狗，还必须在函数调用中 给animal_type 提供实参；
    同样，指定该实参时可以使用位置方式，也可以使用关键字方式。
    """
    print("\npet_name: " + pet_name + " " + "animal_type: " + animal_type + ";")


# 一条名为Willie的小狗
describe_pet('willie')
describe_pet(pet_name='willie')
# 一只名为Harry的仓鼠
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
