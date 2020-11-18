#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/18 20:50
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_6.3.2_dictionaryForKey.py
# @Software: PyCharm

# 遍历字典中左右的键(key)
# 遍历字典时，会默认遍历所有的键
# 方法keys() 并非只能用于遍历，它返回一个列表，其中包含字典中的所有键

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# 方法一
# 更显式的方法，更直观
for name_1 in favorite_languages.keys():
    print(name_1.title())

# 方法二
for name_2 in favorite_languages:
    print(name_2.title())

# 判断字典中的值，是否再列表中存在
friends = ['phil', 'sarah']
for name_3 in favorite_languages.keys():
    print(name_3.title())
    if name_3 in friends:
        print(" Hi " + name_3.title() +
              ", I see your favorite language is " +
              favorite_languages[name_3].title() + "!")
# 输出：
# Sarah
#  Hi Sarah, I see your favorite language is C!
# Edward
# Phil
#  Hi Phil, I see your favorite language is Python!


# 对比字符串，不在字典中的键
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
