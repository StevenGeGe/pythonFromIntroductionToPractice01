# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/12/2 18:59
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : bullet.py
# @Software: PyCharm

# bullet类
# Bullet 类继承了我们从模块pygame.sprite 中导入的Sprite 类。
# 通过使用精灵，可将游戏中相关的元素编组，进而同时操作编组中的所有元素。

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0,
                                ai_settings.bullet_width,
                                ai_settings.bullet_height)
        # 将表示子弹的rect 的top 属性设置为飞船的rect 的top 属性，让子弹看 起来像是从飞船中射出的
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # 存储用小数表示的子弹位置, 以便后期微调，存储子弹颜色和速度
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹,管理更新子弹的位置"""
        # 更新表示子弹位置的小数值
        # 让我们能够随着游戏的进行或根据需要提高子弹的速度，以调整游戏的行 为。
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.centery = self.y
        # 子弹发射后，其 x 坐标始终不变，因此子弹将沿直线垂直地往上穿行。

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
