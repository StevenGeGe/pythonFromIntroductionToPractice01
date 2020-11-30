#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/30 20:53
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : language_survey.py
# @Software: PyCharm

from survey import AnonymousSurvey

# 定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "你最初学的语言是什么?"
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案
my_survey.show_question(question)
print("随时输入“q”退出.\n")
while True:
    response = input("语言: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# 显示调查结果
print("\n感谢所有参与调查的人!")
my_survey.show_results(my_survey.responses)
