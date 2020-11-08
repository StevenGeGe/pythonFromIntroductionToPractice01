#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/8 17:46
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_3.2.3_listDel.py
# @Software: PyCharm

# 列表的修改，添加，删除

# 列表中删除元素
# 根据元素在列表中的位置删除
# del list[索引序号]

# 删除列表末尾元素，但依然可以使用它。
# list.pop()
# 属于弹出(pop), 列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶的元素。

# 根据值删除元素
# list.remove('要删除的元素值')
# list.remove('要删除的元素值'),只删除第一个指定的值。如果要删除的值可能在列表中多次出现，就需要使用循环来判断是否删除了所有这样的值。


# del 根据序号删除元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'dafeng']
print(motorcycles)  # 输出: ['honda', 'yamaha', 'suzuki', 'dafeng']

del motorcycles[0]
print(motorcycles)  # 输出: ['yamaha', 'suzuki', 'dafeng']

del motorcycles[2]
print(motorcycles)  # 输出: ['yamaha', 'suzuki']

# pop 删除列表最后一个元素
motorcycles_1 = ['honda', 'yamaha', 'suzuki', 'dafeng']
print(motorcycles_1)  # 输出: ['honda', 'yamaha', 'suzuki', 'dafeng']
motorcycles_2 = motorcycles_1.pop()
print(motorcycles_2)  # 输出的是最后一个元素 #输出: dafeng
print(motorcycles_1)  # 输出: ['honda', 'yamaha', 'suzuki']

# 根据值删除元素
motorcycles_3 = ['honda', 'yamaha', 'suzuki', 'dafeng']
print(motorcycles_3)  # 输出: ['honda', 'yamaha', 'suzuki', 'dafeng']
motorcycles_3.remove('suzuki')
print(motorcycles_3)  # 输出: ['honda', 'yamaha', 'dafeng']
