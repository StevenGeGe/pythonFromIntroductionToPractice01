#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/30 21:09
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : set_up.py
# @Software: PyCharm

# set_up()

# 如果在TestCase 类中包含了方法setUp() ，Python将先运行它，
#   再运行各个以test_打头的方法。

# set_up() 在此类中的作用
# 1、创建一个调查对象
# 2、创建一个答案列表

# 运行测试用例时，每完成一个单元测试，Python都打印一个字符：
#   测试通过时打印一个句点；
#   测试引发错误时打印一个E ；
#   测试导致断言失败时打印一个F 。
# 这就是你运行测试用例时，在输出的第一行中看到的句点和字符数量各不相同的原因。
# 如果测试用例包含很多单元测试，需要运行很长时间，就可通过观察这些结果 来获悉有多少个测试通过了。


import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def setUp(self):
        """ 创建一个调查对象和一组答案，供使用的测试方法使用 """
        question = "你最初学的语言是什么?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()
