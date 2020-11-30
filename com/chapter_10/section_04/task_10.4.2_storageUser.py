#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/30 19:40
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_10.4.2_storageUser.py
# @Software: PyCharm

# 存储用的数据
# ensure_ascii=False: 避免控制台输入的中文写入到文件中，会显示成Unicode码。

import json

user_name = input("姓名：")
file_name = 'user_name.json'

# 用户的输入作为写入文件的数据
with open(file_name, 'w', encoding='utf-8') as file_object_write:
    json.dump(user_name, file_object_write, ensure_ascii=False)
    print("你回来的时候，我们会记得你，" + user_name + " !")

# 从文件中读取数据
with open(file_name, 'r', encoding='utf-8') as file_object_read:
    user_name_2 = json.load(file_object_read)
    print("欢迎回来: " + user_name_2)

# 加入try-except-else的错误判断
# 如果以前存储了用户名，就加载它
#  否则，就提示用户输入用户名并存储它
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")
