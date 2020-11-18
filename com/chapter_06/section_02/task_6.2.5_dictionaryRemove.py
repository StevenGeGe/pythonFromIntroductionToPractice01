#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/18 18:57
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_6.2.5_dictionaryRemove.py
# @Software: PyCharm

# 删除字典中的k键值对
# 对于字典中不再需要的信息，可使用del 语句将相应的键—值对彻底删除。
# 使用del 语句时，必须指定字典名和要删除的键。

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)  # 输出： {'color': 'green', 'points': 5}

del alien_0['points']
print(alien_0)  # 输出： {'color': 'green'}
