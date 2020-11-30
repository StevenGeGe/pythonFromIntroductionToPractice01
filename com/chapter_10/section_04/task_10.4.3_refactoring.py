#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/30 20:03
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_10.4.3_refactoring.py
# @Software: PyCharm

# 重构
# 将可以正确执行的代码，划分为一些列完成具体工作的函数，这样的过程叫做重构。
# 重构让代码更清晰，更易于理解，更容易扩展。

import json


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
    print("We'll remember you when you come back, " + username + "!")


greet_user()
