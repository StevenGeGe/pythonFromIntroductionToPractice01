#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/8 15:43
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_2.3.4_deleteBlank.py
# @Software: PyCharm

# python3中会识别字符串中多余的空白
# string.rstrip(): 删除字符串末尾的空白
# string.lstrip(): 删除字符串前的空白
# string.strip():  删除字符串两端的空白
# len(str): 计算字符串大小


print(len("nihao"))  # 输出 ：5
print(len("nihao "))  # 输出 ：6

print(len("nihao"))  # 输出 ：5
print(len("nihao ".rstrip()))  # 输出 ：5

# 使用strip()删除字符串前后的空白
name = "  nihao  "
print(name)
print(name.strip())  # 只是删除了临时变量的内容，而不是本身变量的的内容
print(name)
