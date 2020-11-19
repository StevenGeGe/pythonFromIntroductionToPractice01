#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/19 20:03
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_7.1.1_input.py
# @Software: PyCharm

# python3中的输入

# 函数input()：让程序暂停运行，等待用户输入一些文本。
# 获取用户输入后，Python将其存储在一个变量中，以方便你使用。
# input("你想输出的提示信息"), 并把输入的信息返回给其他变量。

# 可将提示存储在一个变量中，再将该变量传递给函数input() 。

message = input("输入你想输入的信息：")
print("你输入的信息是：" + message)

name = input("请在这里输入你的名字: ")
print("Hello, " + name + "!")

# 放在多行输入
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")
