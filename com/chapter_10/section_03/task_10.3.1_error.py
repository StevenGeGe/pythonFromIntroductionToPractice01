#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/26 19:47
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_10.3.1_error.py
# @Software: PyCharm

# 异常处理
# 异常：管理python3执行期间发生的错误的特殊对象
#   如果你编写了处理该异常的代码，程序将继 续运行；
#   如果你未对异常进行处理，程序将停止，并显示一个traceback，其中包含有关异常的报告。
# 实例：
#   try-except


# 错误
# print(5/0)

# 正常, 代码正常进行，返回0
try:
    print(5 / 0)
except ZeroDivisionError:
    print("不能除以0 !", ZeroDivisionError)
