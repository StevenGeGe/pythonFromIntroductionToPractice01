#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/12/1 21:09
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : settings.py
# @Software: PyCharm

# 设置类
# 调整飞船移动速度
# 设置子弹


class Settings:
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 250)
        # 飞船的速度，移动1.5像素
        self.ship_speed_factor = 1.5
        # 子弹设置
        #  宽3像素，高15像素，深灰色子弹。子弹速度比飞船速度稍低
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        # 将未消失的子弹数限制为3颗
        self.bullets_allowed = 3
