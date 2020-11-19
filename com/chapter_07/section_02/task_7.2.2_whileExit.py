#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/19 20:53
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_7.2.2_whileExit.py
# @Software: PyCharm

#  让用户选择退出时间
# 让用户输入一个值，代表程序结束。

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# 添加一个判断，将最后输入的quit， 去掉。
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
