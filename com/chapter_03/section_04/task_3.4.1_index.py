#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/9 20:01
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_3.4.1_index.py
# @Software: PyCharm

# 使用列表时，避免索引错误
# 索引从0 开始，而不是从1 开始。
# 索引 -1， 访问列表中最后一个元素。
# 如果列表为空， 用-1 访问最后一个元素，也会发生越界错误。

# 发生索引错误找不到解决办法时，可以将列表或列表的长度打印出来。


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  # 输出： ['honda', 'yamaha', 'suzuki']

# 用-1， 访问列表中最后一个元素
print("用-1， 访问最后一个元素：", end="")
print(motorcycles[-1])  # 输出： suzuki

# 用0， 访问列表中 第一个元素
print("用0， 访问第一个元素：", end="")
print(motorcycles[0])  # 输出： honda

# 当列表为空时， 用-1， 访问会发生越界错误
del motorcycles[:]
print("清空列表后用-1，访问最后一个元素：", end="")
# print(motorcycles[-1])   #输出： 会越界报错
