#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/18 21:22
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_6.3.3_dictionarySorted.py
# @Software: PyCharm

# 顺序获取字典中所有的键

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby', 'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# 输出：
# Edward, thank you for taking the poll.
# Jen, thank you for taking the poll.
# Phil, thank you for taking the poll.
# Sarah, thank you for taking the poll.
