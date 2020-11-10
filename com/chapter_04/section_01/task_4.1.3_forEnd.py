#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/10 21:31
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_4.1.3_forEnd.py
# @Software: PyCharm

# for循环
# 只要在for循环结束的下一行，不再缩进，则代表循环体结束。

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick" + magician.title() + ".\n");

print("end")
