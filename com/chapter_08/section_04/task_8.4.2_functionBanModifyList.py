#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/23 19:16
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_8.4.2_functionBanModifyList.py
# @Software: PyCharm

# 禁止函数修改列表
# 将列表的副本传给函数
# def function_name(list_name[:])
# 函数使用现成列表可避免花时间和内存创 建副本，从而提高效率，在处理大型列表时尤其如此。


# 报错未知
# def print_models(unprinted_designs[:]):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print("打印模型: " + current_design)
#         completed_models.append(current_design)
