#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/18 20:37
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_6.3.1_dictionaryFor.py
# @Software: PyCharm

# 遍历字典

# Python支持对字典遍历。
# 字典可用于以各种方式存储信息，
# 因此有多种 遍历字典的方式：可遍历字典的所有键—值对、键或值。
# dictionary.items(): 返回一个键值对列表。
# 便遍历字典时，键—值对的返回顺序也与存储顺序不同。

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print("Key:" + key + " ", end="")
    print("Value:" + value)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
