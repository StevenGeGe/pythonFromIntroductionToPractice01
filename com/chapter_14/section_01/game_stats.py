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
        # 游戏刚启动时处于活动状态
        self.game_active = True
        # 在任何情况下都不应重置最高得分
        self.high_score = 0

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
