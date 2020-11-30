#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/30 20:28
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_11_1_2_testModule.py
# @Software: PyCharm

# 测试模块
# 文件名称不要有多余的句号(.)， 否则会找不到函数。
# self.assertEqual(): 断言方法；
#   断言方法用来核实得到的结果是否与期望的结果一致。
#   如果不一致，也不会报错。
import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')  # 断言


unittest.main()
