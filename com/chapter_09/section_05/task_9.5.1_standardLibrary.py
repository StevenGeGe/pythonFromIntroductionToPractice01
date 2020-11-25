#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/25 20:51
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_9.5.1_standardLibrary.py
# @Software: PyCharm

# python3中的标准库
# Python标准库 标 是一组模块，安装的Python都包含它。
# 标准库： https://pymotw.com/3/

# 创建字典并记录其中的键—值对的添加顺序
from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

# 输出：
# Jen's favorite language is Python.
# Sarah's favorite language is C.
# Edward's favorite language is Ruby.
# Phil's favorite language is Python.
