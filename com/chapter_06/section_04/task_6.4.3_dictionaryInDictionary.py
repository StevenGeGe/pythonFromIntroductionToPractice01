#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/19 19:47
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_6.4.3_dictionaryInDictionary.py
# @Software: PyCharm

# 在字典中存储字典


users = {
    'a.einstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'm.curie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

# 将字典中的键值对，返回给临时变量
for user_name, user_info in users.items():
    print("\nuser_name: " + user_name)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("Full name: " + full_name.title())
    print("\tLocation: " + location.title())
