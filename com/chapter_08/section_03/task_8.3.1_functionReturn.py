#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/20 20:57
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_8.3.1_functionReturn.py
# @Software: PyCharm

# 函数返回值
# 函数将处理的数据，返回一个或者一组值，称为函数的返回值。
# 使用return 语句将值返回到调用函数的代码行。
# 返回值让你能够将程序的大部分繁重工作移到函数中去完成，从而简化主程序。


def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
