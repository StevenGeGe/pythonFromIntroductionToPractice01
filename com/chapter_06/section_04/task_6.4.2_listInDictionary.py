#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/19 18:36
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_6.4.2_listInDictionary.py
# @Software: PyCharm

# 在字典中存储列表
# 列表和字典的嵌套层级不应太多。
# 如果嵌套层级比前面的示例多得多，很可能有更简单的解决问题的方案。

# 存储披萨所点的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# 概述所点披萨
print(("You ordered a " + "\"" +
       pizza['crust'] + "\"" +
       "-crust pizza " +
       "with the following toppings:"))
for topping in pizza['toppings']:
    print("\t" + topping)

# 字典中嵌套多个列表
favorite_languages = {'jen': ['python', 'ruby'],
                      'sarah': ['c'],
                      'edward': ['ruby', 'go'],
                      'phil': ['python', 'haskell'],
                      }

# 获取所有的键值对列表
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite language are:")
    for language in languages:
        print("\t" + language.title())
