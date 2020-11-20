#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/20 21:12
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_8.3.3_functionReturnDictionary.py
# @Software: PyCharm

# 函数返回字典
# 函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。


def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person


print(build_person('jimi', 'hendrix'))
