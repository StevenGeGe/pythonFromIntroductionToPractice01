#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/8 17:21
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_3.2.1_listMod.py
# @Software: PyCharm

# 列表的修改，添加，删除

# 修改元素列表
# 修改元素列表的语法与访问列表元素的语法类似。
# 要修改列表元素，可指定列表名和要修改的元素的索引，再指定改元素的新值。
# 直接找到索引直接修改

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  # 输出: ['honda', 'yamaha', 'suzuki']

# 修改元素列表
motorcycles[0] = 'ducati'
print(motorcycles)  # 输出: ['ducati', 'yamaha', 'suzuki']
