#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/19 17:41
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_6.4.1_dictionaryList.py
# @Software: PyCharm

# 字典中的嵌套

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
# 输出：
# {'color': 'green', 'points': 5}
# {'color': 'yellow', 'points': 10}
# {'color': 'red', 'points': 15}


print("...")

# 创建一个空的列表，用来存储字典
aliens = []
# 往列表里面添加字典数据
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': alien_number, 'speed': 'slow'}
    aliens.append(new_alien)

# 打印列表中前五个字典
for alien in aliens[:5]:
    print(alien)
print("...")

# 显示创建了具体的外星人
print("Total number of aliens: " + str(len(aliens)))

# 和for ， if 连用
# 创建一个存储外星人的空列表
aliens = []

# 创建30个外星人
for alien_number in range(0, 30):
    new_alien = {'color': 'green', 'points': alien_number, 'speed': 'slow'}
    aliens.append(new_alien)

# 修改前三个外星人状态
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# 显示前5个外星人
print("不一样的5个外星人")
for alien in aliens[:5]:
    print(alien)
print("不一样的5个外星人")
