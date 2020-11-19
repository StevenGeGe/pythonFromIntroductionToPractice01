#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/19 20:29
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_7.1.2_inputInt.py
# @Software: PyCharm

# int类型数值输入

# 默认输入类型为string类型
age = input("输入你的年龄： ")
print(age)

# 会报错
# if 12 >= age:
#    print("比12岁小")
# else:
#   print("不比12岁小")

# 做出修改
age_int = int(age)
if age_int >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
