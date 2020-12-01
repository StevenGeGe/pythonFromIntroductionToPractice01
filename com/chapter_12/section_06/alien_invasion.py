#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/12/1 19:26
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : alien_invasion.py
# @Software: PyCharm

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ship)
        ship.update()
        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings, screen, ship)


run_game()
