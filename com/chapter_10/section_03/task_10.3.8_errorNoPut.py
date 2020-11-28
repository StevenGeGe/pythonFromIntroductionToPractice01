#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/26 21:04
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_10.3.8_errorNoPut.py
# @Software: PyCharm

# 遇到错误不输出， 并继续运行
# pass： 不做任何操作，直接退出，继续执行
#       还充当占位符，提示未做任何操作。

# 对于异常，自己决定到底是否要打印信息


# 分析多个文件
def count_words(file_name):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(file_name, encoding="utf-8") as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("这本书 " + file_name + " 大约有 " + str(num_words) + " 字.")


# 处理多个文件
file_names = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for file in file_names:
    count_words(file)
# 输出： 这本书 alice.txt 大约有 29465 字.
