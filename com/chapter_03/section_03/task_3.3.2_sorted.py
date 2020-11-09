#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/9 19:10
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_3.3.2_sorted.py
# @Software: PyCharm

# 列表中的排序

# 列表中排序，临时改变顺序，不更改列表的原始的顺序
# sorted(list): 临时对列表的内容排序，不改变原始数据
# 默认正序
# 如果想倒序，sorted(list, reverse=True), 输入reverse=True 即可。

carList = ['bmw', 'audi', 'toyota', 'subaru']
print("初始顺序：")
print(carList)  # 输出: ['bmw', 'audi', 'toyota', 'subaru']
print("临时顺序：")
print(sorted(carList))  # 输出: ['audi', 'bmw', 'subaru', 'toyota']
print("最终顺序：")
print(carList)  # 输出: ['bmw', 'audi', 'toyota', 'subaru']
print("临时倒序：")
print(sorted(carList, reverse=True))  # 输出: ['toyota', 'subaru', 'bmw', 'audi']
