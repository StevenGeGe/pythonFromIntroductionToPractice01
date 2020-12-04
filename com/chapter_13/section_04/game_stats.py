#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/12/4 19:58
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : game_stats.py
# @Software: PyCharm


class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
