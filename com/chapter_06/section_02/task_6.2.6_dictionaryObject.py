#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/18 19:28
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_6.2.6_dictionaryObject.py
# @Software: PyCharm

# 字典存储的是一个对象
# 定义好字典后，在最后一个键—值对的下一行添加一个右花括号，并缩进四个空格，
# 使其与字典中的键对齐

# 另外一种不错的做法是在最后一个键—值对后面也加上逗号，
# 为以 后在下一行添加键—值对做好准备。

# 对于较长的列表和字典，大多数编辑器都有以类似方式设置其格式的功能

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print(favorite_languages)

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() + ".")
