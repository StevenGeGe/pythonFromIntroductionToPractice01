#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/16 20:47
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_5.3.6_ifTest.py
# @Software: PyCharm

# 有时候必须检查你关心的所有条件。
# 在这种情况下，应使用一系列不包含elif 和else 代码块的简单if 语句。
# 在可能有多个条件为True ，且你需要在每个条件为True 时都采取相应措施时，适合使用这种方法。

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
# 输出：Adding mushrooms.
# 输出：Adding extra cheese.
# 输出：Finished making your pizza!
