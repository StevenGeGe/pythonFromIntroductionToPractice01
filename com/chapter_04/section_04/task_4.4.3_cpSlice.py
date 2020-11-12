#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/12 20:00
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_4.4.3_cpSlice.py
# @Software: PyCharm

# 复制切片
# list[:] : 代表整个list，也代表整个切片
# 使用切片复制列表， 会新建一个list
# 直接复制列表， 不会新建一个list，只是副本，随着原始数据的改变而改变

my_foods = ['pizza', 'coffee', 'cake']
# 用切片复制列表
friend_foods = my_foods[:]
friend_foods.append('red')

print("my_foods:", end='')
print(my_foods)  # 输出： ['pizza', 'coffee', 'cake']
print("friend_foods:", end='')
print(friend_foods)  # 输出： ['pizza', 'coffee', 'cake', 'red']

# 不用切片复制， 而是直接赋值
# list =  list： 只是复制了一个临时副本，而不是新建一个列表
friend_foods_2 = my_foods
print(friend_foods_2)  # 输出： ['pizza', 'coffee', 'cake']
friend_foods_2.append('ice')
print(friend_foods_2)  # 输出： ['pizza', 'coffee', 'cake', 'ice']
print(my_foods)  # 输出： ['pizza', 'coffee', 'cake', 'ice']
