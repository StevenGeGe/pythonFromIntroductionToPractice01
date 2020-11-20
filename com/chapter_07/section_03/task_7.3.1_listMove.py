#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/20 18:11
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_7.3.1_listMove.py
# @Software: PyCharm

# 在多个列表之间移动元素
# list.pop(): 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。

# 首先，创建一个待验证用户列表
#  和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# 显示所有已验证的用户
print("\n以下用户已经确认:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
