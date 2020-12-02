#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/12/1 20:38
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : game_functions.py
# @Software: PyCharm

# 响应按键
# 修改了游戏在玩家按下右箭头键时响应的方式：
#   不直接调整飞船的位置，而只是将moving_right 设置为True 。
#   添加了一个新的elif 代码块，用 于响应KEYUP 事件：玩家松开右箭头键（K_RIGHT ）时，我们将moving_right 设置为False 。


import sys
import pygame


def check_keydown_events(event, ship):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
