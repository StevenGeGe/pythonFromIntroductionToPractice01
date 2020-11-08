#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/8 16:37
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_3.1.1_list.py
# @Software: PyCharm

# 列表
# 列表是由一系列特定顺序排列的元素组成。
# 可以将任何东西加入到列表中，其中的元素可以没有任何关系，无论是字母，数字，家庭成员姓名。
# 通常用（[]）来表示列表， 并用逗号分隔其中的元素。

# 访问列表
# 列表是有序集合，若访问列表中的任何元素，只需将该元素的位置或者索引告诉python即可。
# 要访问列表元素，可指出列表的名称，再指出元素的索引，并将其放在括号内。

# 列表索引访问
# 在python3中，第一个元素的所索引为0，而不是1。这与列表操作的底层实现相关。
# 访问第一个元素，为0； 访问第二个元素，为1； 访问最后一个元素，为-1。

# 列表的写法
bicycles_1 = ['a', 'b', 'c', 'd']
print(bicycles_1)  # 输出: ['a', 'b', 'c', 'd']

bicycles_2 = ["aa", "bb", "cc", "dd"]
print(bicycles_2)  # 输出:  ['aa', 'bb', 'cc', 'dd']

bicycles_3 = ["aa" "bb" "cc""dd"]
print(bicycles_3)  # 输出:  ['aabbccdd']

# 访问列表元素
bicycles_4 = ['a', 'b', 'c', 'd']
print(bicycles_4[0])  # 输出: a

bicycles_4 = ['aa', 'bb', 'cc', 'dd']
print(bicycles_4[0].title())  # 输出: Aa

# 索引访问
bicycles_5 = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles_5[-1])  #输出: specialized
