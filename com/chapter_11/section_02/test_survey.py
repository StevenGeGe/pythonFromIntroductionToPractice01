#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/30 21:03
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : test_survey.py
# @Software: PyCharm

# 测试AnonymousSurvey 类

import unittest
from survey import AnonymousSurvey


class TestAnonmyousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        question = "你最初学的语言是什么?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('英语')
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)


unittest.main()
