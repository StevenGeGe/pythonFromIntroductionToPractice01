#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/19 21:00
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_7.2.3_whileMark.py
# @Software: PyCharm

# 使用标志退出while循环
# 定义一个变量，用于判断整个程序是否处于活动状态。这个变量被称为标志。
# 让程序在标志 为True 时继续运行，并在任何事件导致标志的值为False 时让程序停止运行。
# 在while 语句中就只需检查一个条件——标志的当前值是否为True ，
# 并将所有测试（是 否发生了应将标志设置为False 的事件）都放在其他地方，
# 从而让程序变得更为整洁。

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
