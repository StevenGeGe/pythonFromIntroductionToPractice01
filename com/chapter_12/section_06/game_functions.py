#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/12/1 20:38
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : game_functions.py
# @Software: PyCharm

# 相应按键


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
                ship.rect.centerx += 2


def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
