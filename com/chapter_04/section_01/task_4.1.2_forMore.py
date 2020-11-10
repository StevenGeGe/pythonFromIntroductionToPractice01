#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/10 21:11
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_4.1.2_forMore.py
# @Software: PyCharm

# for循环打印列表中内容
# 在for后面多家一些元素输出。

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick" + magician.title() + ".\n");
