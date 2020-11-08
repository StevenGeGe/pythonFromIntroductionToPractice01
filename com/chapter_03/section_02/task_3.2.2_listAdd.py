#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/8 17:29
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_3.2.2_listAdd.py
# @Software: PyCharm

# 列表的修改，添加，删除

# 在列表后面追加元素
# list.append('元素名称'): 列表添加元素方法。

# 在列表中插入元素
# 根据新元素的索引和值插入列表
# list.inster('新元素')


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  # 输出: ['honda', 'yamaha', 'suzuki']

# 追加元素
motorcycles.append("dafeng")
print(motorcycles)  # 输出: ['honda', 'yamaha', 'suzuki', 'dafeng']

# 追加元素
motorcycles_1 = []
print(motorcycles_1)  # 输出: []
motorcycles_1.append('suzuki')
motorcycles_1.append('yamaha')
print(motorcycles_1)  # 输出: ['suzuki', 'yamaha']

# 插入元素
motorcycles_2 = ['honda', 'yamaha', 'suzuki']
print(motorcycles_2)  # 输出: ['honda', 'yamaha', 'suzuki']
motorcycles_2.insert(0, 'ducati')
print(motorcycles_2)  # 输出: ['ducati', 'honda', 'yamaha', 'suzuki']
