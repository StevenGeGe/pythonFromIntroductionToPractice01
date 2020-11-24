#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/24 15:36
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_8.6.5_importAll.py
# @Software: PyCharm

# 导入所有函数
# 使用(*) 星号运算符 可让python导入模块中所有的函数

# 使用 并非自己编写的大型模块时，最好不要采用这种导入方法
# 如果模块中有函数的名称与你的项目中使用的名称相同，可能导致意想不到的结果
# Python可能遇到多个名称相同的函 数或变量，进而覆盖函数，而不是分别导入所有的函数。

# 最佳做法，选择一种即可：
#   1、只导入你需要使用的函数
#   2、导入整个模块并使用句点表示法

from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
