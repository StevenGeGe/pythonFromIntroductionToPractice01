#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/12/1 18:46
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : settings.py
# @Software: PyCharm

# 设置类
#  优点
#   1、用于统一存储其他的配置，后面调用只需传递一个设置对象即可。
#   2、让函数调用更简单
#   3、降低修改配置的难度


class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 250)
