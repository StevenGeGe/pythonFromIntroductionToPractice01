#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/20 20:11
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_8.1.2_functionParameter.py
# @Software: PyCharm

# 函数的参数传递
# 参数： 形参，实参
# 在函数great_user_name()中，要求给变量username 指定一个值。
# 变量username 是一个形参，也就是函数完成其工作所需的一项信息。

# 在代码greet_user('丽芳') 中，值'丽芳' 是一个实参。
# 实参是 调用函数时传递给函数的信息

def great_user(user_name):
    print("hello, " + user_name + ".")


# 调用函数
great_user("丽芳")
