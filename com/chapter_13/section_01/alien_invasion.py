#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/12/1 19:26
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : alien_invasion.py
# @Software: PyCharm

# pygame.sprite.Group 类类似于列表，但提供了有助于开发游戏的额外功 能。
# 将输出写入到终端而花费的时间比将图形绘制到游戏窗口花费的时间还多。

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    # 创建一个screen窗口
    pygame.display.set_caption("Alien Invasion")
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人
    alien = Alien(ai_settings, screen)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings=ai_settings, screen=screen, ship=ship, bullets=bullets)
        ship.update()
        gf.update_bullets(bullets=bullets)
        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings=ai_settings, screen=screen, ship=ship, alien=alien, bullets=bullets)


run_game()
