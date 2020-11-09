#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/9 19:35
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_3.3.3_reverse.py
# @Software: PyCharm

# 列表的排序

# 不是对列表的排序， 只是反转元素的排列顺序。
# list.reverse(): 永久性的修改列表元素的排列顺序， 但是可以随时恢复到原来的排列顺序，
# 恢复原来的排列顺序，只需对列表再次使用reverse() 即可。


carList = ['bmw', 'audi', 'toyota', 'subaru']
print("初始顺序：")
print(carList)  # 输出: ['bmw', 'audi', 'toyota', 'subaru']

carList.reverse()
print("倒序打印：")
print(carList)  # 输出: ['subaru', 'toyota', 'audi', 'bmw']

carList.reverse()
print("恢复原始顺序：")
print(carList)  # 输出: ['bmw', 'audi', 'toyota', 'subaru']
