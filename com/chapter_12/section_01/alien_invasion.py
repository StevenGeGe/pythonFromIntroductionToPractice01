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

import sys
import pygame

screen_width = 1000
screen_height = 600


def run_gane():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Alien invasion")

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_gane()
