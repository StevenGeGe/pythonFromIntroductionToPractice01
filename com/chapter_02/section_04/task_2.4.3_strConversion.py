#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/8 16:21
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_2.4.3_strConversion.py
# @Software: PyCharm

# 整形变量转换成字符串
# str()

# 错误用法
# age = 20
# message= "Happy " + age + "rd Birthday"
# print(message)

# import this

# 正确用法， 需要先将int类型的数据转换成字符串类型
age2 = 20
message2 = "Happy " + str(age2) + "rd Birthday"
print(message2)  # 输出:  Happy 20rd Birthday
