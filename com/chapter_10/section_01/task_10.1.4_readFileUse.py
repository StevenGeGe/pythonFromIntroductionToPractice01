#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/26 18:19
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_10.1.4_readFileUse.py
# @Software: PyCharm

# 将文件中的内容存储到列表中
# 如果读取的是数字，并作为数值使用，可用int()函数转换为整数，
#   或者是使用float() 函数转换为浮点数。
file_name = "pi_digits.txt"

with open(file_name) as file_object:
    lines = file_object.readlines()  # 读取所有行
    # lines = file_object.readline()  # 读取一行

for line in lines:
    print(line.rstrip())

# 输出：
# 3.1415926535
# 8979323846
# 2643383279

# 使用列表中的内容
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string, "大小：", len(pi_string))
# 输出： 3.141592653589793238462643383279 大小： 32

# 删除每行最左边的空格
pi_string_2 = ''
for line_2 in lines:
    pi_string_2 += line_2.strip()
print(pi_string_2, "大小：", len(pi_string_2))
# 输出： 3.141592653589793238462643383279 大小： 32

# 转换为浮点数
pi_float = float(pi_string_2)
print(pi_float)
# 输出： 3.141592653589793
