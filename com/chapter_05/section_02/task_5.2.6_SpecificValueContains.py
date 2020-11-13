#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/13 20:24
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_5.2.6_SpecificValueContains.py
# @Software: PyCharm

# 检查特定值是否包含
# 可以用in， 检查特定值是否包含在该列表中

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)  # 输出: True
print('pepperoni' in requested_toppings)  # 输出: False

# 检查特定的值是否不包含在其中
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ', yuo can post a response if you wish.')
    # 输出： Marie, yuo can post a response if you wish.
