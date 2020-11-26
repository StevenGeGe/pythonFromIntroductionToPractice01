#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/26 20:57
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_10.4.7_errorAnalysisAnyFile.py
# @Software: PyCharm

# 分析多个文件
def count_words(file_name):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(file_name, encoding="utf-8") as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("抱歉 ", file_name, "这个文件不存在")
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("这本书 " + file_name + " 大约有 " + str(num_words) + " 字.")


# 处理单个文件
file_name = 'alice.txt'
count_words(file_name)

# 处理多个文件
file_names = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for file in file_names:
    count_words(file)
# 输出：
# 这本书 alice.txt 大约有 29465 字.
# 抱歉  siddhartha.txt 这个文件不存在
# 抱歉  moby_dick.txt 这个文件不存在
# 抱歉  little_women.txt 这个文件不存在
