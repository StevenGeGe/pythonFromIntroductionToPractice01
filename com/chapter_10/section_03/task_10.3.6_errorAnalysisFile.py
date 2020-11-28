#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/26 20:44
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_10.3.6_errorAnalysisFile.py
# @Software: PyCharm

# 分析文本
# split(): 根据一个字符串创建一个单词列表
#   以空格为分隔符，将字符串分成多个部分，并将这些部分存储到列表中。

file_name = 'alice.txt'
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
    # print(contents)
# 输出： 这本书 alice.txt 大约有 29465 字.
