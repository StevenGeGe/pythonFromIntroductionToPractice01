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
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    # 创建一个screen窗口
    pygame.display.set_caption("Alien Invasion")
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人编组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings=ai_settings, screen=screen, ship=ship, aliens=aliens)
    # 创建存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings=ai_settings, screen=screen, stats=stats, sb=sb,
                        play_button=play_button, aliens=aliens, ship=ship, bullets=bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings=ai_settings, screen=screen, stats=stats, sb=sb,
                              ship=ship, aliens=aliens, bullets=bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings=ai_settings, screen=screen, stats=stats, sb=sb,
                         ship=ship, aliens=aliens, bullets=bullets, play_button=play_button)


run_game()
