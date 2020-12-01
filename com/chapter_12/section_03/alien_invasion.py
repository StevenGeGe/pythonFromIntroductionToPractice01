#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/12/1 15:52
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : alien_invasion.py
# @Software: PyCharm

# 宽：1000像素
# 高：600像素
# pygame.display.flip(): 绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见.
#   将不断更新屏幕，以显示元素的新位置，并在原来的位置隐藏元素，从而营造平滑移动的效果。
# screen.fill(): 用背景色填充屏幕；只接受一个实参：一种颜色。

# from settings import Settings: 导入配置类

import sys
import pygame

from settings import Settings


def run_gane():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_gane()
