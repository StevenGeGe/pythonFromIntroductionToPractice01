#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/26 20:20
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_10.3.3_errorUse.py
# @Software: PyCharm

# 使用异常，避免崩溃

print("给我两个数，我来除以它们.")
print("输入“q”退出.")
# 异常较多
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     answer = int(first_number) / int(second_number)
#     print(answer)

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("不能除以0!")
        # 当除数是0是，会出现此报错。
    except Exception:
        print("其它错误")
        # 当输入的是非数字时，会出现此报错。
    else:
        print(answer)
