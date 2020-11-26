#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/26 18:52
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_10.1.5_readFileMillion.py
# @Software: PyCharm

# 读取万行的数据文件， 包含百万位的数据

file_name = "pi_million_digits.txt"

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string[:52] + "...")
print("大小：", len(pi_string))

# 查看圆周率中是是否包含自己的生日
birthday = input("输入你的生日：")
if birthday in pi_string:
    print("你的生日出现在圆周率的第一个百万位数")
else:
    print("你的生日不会出现在圆周率的第一个百万位数中")
