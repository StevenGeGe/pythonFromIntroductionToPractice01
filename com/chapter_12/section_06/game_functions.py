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


def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # 向右移动飞船,2个像素
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
