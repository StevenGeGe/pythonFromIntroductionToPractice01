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
        self.bg_color = (230, 230, 230)
        # 飞船的速度，
        self.ship_limit = 3
        # 子弹设置
        #  宽3像素，高15像素，深灰色子弹。子弹速度比飞船速度稍低
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 10
        # 将未消失的子弹数限制为3颗
        self.bullets_allowed = 3
        # 外星人设置
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        # 初始化随 游戏进行而变化的属性
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction为1表示向右；为-1表示向左
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
