#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/20 21:06
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_8.3.2_functionChoose.py
# @Software: PyCharm

# 让实参变成可选的
# 可选值让函数能够处理各种不同情形的同时，确保函数调用尽可能简单。


def get_formatted_name(first_name, middle_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)


# 变成可选的
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    """给其中一个值添加一个空的字符串"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


# 调用这个函数时，如果只想指定名和姓，调用起来将非常简单。
# 如果还要指定中间名，就必须确保它是最后一个实参，
# 这样Python才能正确地将位置实参关联到形参
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
