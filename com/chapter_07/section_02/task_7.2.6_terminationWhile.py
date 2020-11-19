#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/19 21:14
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_7.2.6_terminationWhile.py
# @Software: PyCharm

# 避免无限循环
# 每个while 循环都必须有停止运行的途径，这样才不会没完没了地执行下去。
# 要避免编写无限循环，务必对每个while 循环进行测试，确保它按预期那样结束。如果你希望程序在用户输入特定值时结束，可运行程序并输入这样的值；
# 如果在这种情况下程 序没有结束，请检查程序处理这个值的方式，
# 确认程序至少有一个这样的地方能让循环条件为False 或让break 语句得以执行。

x = 1
while x <= 5:
    print(x)
    x += 1
