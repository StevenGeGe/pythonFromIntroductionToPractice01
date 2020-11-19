#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/19 21:05
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_7.2.4_whileBreak.py
# @Software: PyCharm

# 在python3中，break退出while循环
# 立即退出while 循环，不再运行循环中余下的代码，也不管条件测试的结果如何
# break 语句用于控制程序流程，可使用它来控制哪些代码行将执行，
# 哪些代码行不执行，从而让程序按你的要求执行你要执行的代码。

# 在任何Python循环中都可使用break 语句。
# 例如，可使用break 语句来退出遍历列表或字典的for 循环。

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
