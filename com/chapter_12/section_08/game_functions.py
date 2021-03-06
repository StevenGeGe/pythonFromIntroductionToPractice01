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

from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹，并将其加入到编组bullets中
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ai_settings, screen, ship, bullet):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings, screen, ship, bullets)


def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.bitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        # ship.bitme
    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()
    # 删除已消失的子弹
    # 在for 循环中，不应从列表或编组中删除条目，因此必须遍历编组的副本。
    # 我们使用了方法copy() 来设置for 循环
    for bullet in bullets.copy():
        # 如果子弹到顶端则删除
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        # print(len(bullets))  # 打印输出剩余的子弹数量


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    # 创建新子弹，并将其加入到编组bullets中
    # 如果len(bullets) 小于3，我们就创建一个新子弹；
    #   但如果已有3颗未消失的子弹，则玩家按空格键时什么都不会发生。
    #   如果你 现在运行这个游戏，屏幕上最多只能有3颗子弹。
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings=ai_settings, screen=screen, ship=ship)
        bullets.add(new_bullet)
