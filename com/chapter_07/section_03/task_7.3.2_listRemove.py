#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/20 18:19
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_7.3.2_listRemove.py
# @Software: PyCharm

# 删除列表中所有包含特定的值
# list.remove()： 删除列表中的特定值, 从列表首位开始删除。

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

# 从列表首位开始匹配删除
i = 0
while 'cat' in pets:
    pets.remove('cat')
    print(str(i) + ":", end="")
    print(pets)
    i += 1
print(pets)
