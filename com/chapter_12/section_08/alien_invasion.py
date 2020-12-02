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
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        # 删除已消失的子弹
        # 在for 循环中，不应从列表或编组中删除条目，因此必须遍历编组的副本。
        # 我们使用了方法copy() 来设置for 循环
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))
        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
