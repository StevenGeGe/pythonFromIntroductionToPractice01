#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/18 21:27
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_6.3.4_dictionaryForValue.py
# @Software: PyCharm

# 遍历字典中所有的值
# dictionary.value(): 返回一个值列表，而不包含任何键。

# set(): 集合类似于列表，但是每个元素的都是独一无二的，会自动删除重复项。

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("列表：The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
# 输出：
# 列表：The following languages have been mentioned:
# Python
# C
# Ruby
# Python


# 集合
print("集合：The following languages have been mentioned:")
for language_set in set(favorite_languages.values()):
    print(language_set.title())
# 输出集合：
# The following languages have been mentioned:
# Python
# Ruby
# C
