#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/30 20:47
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : survey.py
# @Software: PyCharm

# 测试类


class AnonymousSurvey:
    """收集匿名调查问卷的答案"""

    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self, question):
        """显示调查问卷"""
        print(question)

    def store_response(self, new_response):
        """存储单份调查答卷"""
        self.responses.append(new_response)

    def show_results(self, responses):
        """显示收集到的所有答卷"""
        print("Survey results:")
        for response in responses:
            print('- ' + response)
