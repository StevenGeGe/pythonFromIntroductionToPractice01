#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/9 18:56
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_3.3.1_sort.py
# @Software: PyCharm

# 列表中的排序

# 列表中排序，根据大小写进行排序
# list.sort(): 永久性排序，排序后，无法恢复原来的排序顺序。
# 默认正序
# 若果想倒序，

# 复习上节内容
carList = ['bmw', 'audi', 'toyota', 'subaru']
print(carList.__str__().title())  # 输出: ['Bmw', 'Audi', 'Toyota', 'Subaru']

# 默认正序
carList.sort()
print(carList)  # 输出: ['audi', 'bmw', 'subaru', 'toyota']

# 倒序
carList.sort(reverse=True)
print(carList)  # 输出: ['toyota', 'subaru', 'bmw', 'audi']
