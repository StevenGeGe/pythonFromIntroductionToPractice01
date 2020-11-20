#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/20 18:35
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_7.3.3_listInput.py
# @Software: PyCharm

# 使用用户输入的内容来填充字典

responses = {}

# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\n姓名：")
    response = input("你想爬那座山：")
    # 将答卷存储在字典中
    responses[name] = response
    # 看看是否还有人要参与调查
    repeat = input("还有人想继续参加吗? (yes/ no) ")
    if repeat == 'no' or \
            repeat == 'NO' or \
            repeat == 'No' or \
            repeat == 'nO':
        polling_active = False

# 调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " 喜欢爬 " + response + ".")
