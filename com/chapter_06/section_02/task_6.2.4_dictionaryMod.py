#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/17 20:24
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_6.2.4_dictionaryMod.py
# @Software: PyCharm

# 字典的修改

alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
# 输出： The alien is green.

alien_0['color'] = 'yellow'
print("The alien is " + alien_0['color'] + ".")
# 输出： print("The alien is " + alien_0['color'] + ".")


# 字典修改进阶
alien_1 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_1['x_position']))
# 向右移动外星人 # 据外星人当前速度决定将其移动多远
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的速度一定很快
    x_increment = 3
#  新位置等于老位置加上增量
alien_1['x_position'] = alien_1['x_position'] + x_increment
print("New x-position: " + str(alien_1['x_position']))
