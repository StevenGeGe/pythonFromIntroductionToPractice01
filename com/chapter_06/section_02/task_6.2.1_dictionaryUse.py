#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/17 20:04
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_6.2.1_dictionaryUse.py
# @Software: PyCharm

# 字典的使用
# 在python3中，字典是一系列键-值对。
# 每个键都与一个值相关联。可以使用键来访问与之相关联的值。
# 与键相关联的值可以是数字，字符串，列表乃至字典。
# 可以将任何python对象用作字典中的值。

# 在Python中，字典用放在花括号{} 中的一系列键—值对表示
# 键—值 对是两个相关联的值。
# 指定键时，Python将返回与之相关联的值。
# 键和值之间用冒号分隔，而键—值对之间用逗号分隔。在字典中，
# 你想存储多少个键—值对都可以。 最简单的字典只有一个键—值对

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'green'}

# 访问字典的值
# 要获取与键相关联的值，可依次指定字典名和放在方括号内的键
alien_2 = {'color': 'green'}
print(alien_2['color'])
