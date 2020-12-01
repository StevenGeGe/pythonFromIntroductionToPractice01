#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/12/1 19:13
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : ship.py
# @Software: PyCharm

# 创建ship类
# 1、Pygame的效率之所以如此高，一个原因是它让你能够像处理矩形（rect 对象）一样处理游戏元 素，即便它们的形状并非矩形
# 2、像处理矩形一样处理游戏元素之所以高效，是因为矩形是简单的几何形状。
# 3、处理rect 对象时，可使用矩形四角和中心的 x 和 y 坐标。可通过设置这些值来指定矩形的位置。
# 4、要将游戏元素居中，可设置相应rect 对象的属性center 、centerx 或centery 。
#   要让游戏元素与屏幕边缘对齐，可使用属性top 、bottom 、left 或right ；
#   要调整游 戏元素的水平或垂直位置，可使用属性x 和y ，它们分别是相应矩形左上角的 x 和 y 坐标。
# 5、在Pygame中，原点(0, 0)位于屏幕左上角，向右下方移动时，坐标值将增大。
#   在1200×800的屏幕上，原点位于左上角，而右下角的坐标为(1200, 800)。
import pygame


class Ship:

    def __init__(self, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
