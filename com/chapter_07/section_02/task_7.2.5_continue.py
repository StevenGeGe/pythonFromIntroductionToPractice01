#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/19 21:09
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_7.2.5_continue.py
# @Software: PyCharm

# 在python3中，使用continue
# continue： 结束本次循环，开始下次循环

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
# 输出：
# 1
# 3
# 5
# 7
# 9
