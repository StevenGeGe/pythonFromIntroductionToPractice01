#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/23 20:36
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_8.6.1_module.py
# @Software: PyCharm

# 将函数存储在模块中
# 函数的优点之一是，使用它们可将代码块与主程序分离。
# 通过给函数指定描述性名称，可让主程序容易理解得多

# 还可以更进一步，将函数存储在被称为模块模 的独立文件中， 再将模块导入导 到主程序中。
# import 语句允许在当前运行的程序文件中使用模块中的代码。
# 优点：
#   通过将函数存储在独立的文件中，可隐藏程序代码的细节，将重点放在程序的高层逻辑上。
#   还能让你在众多不同的程序中重用函数
#   可与其他程 序员共享这些文件而不是整个程序。
#   知道如何导入函数还能让你使用其他程序员编写的函数库。

# 模 是扩展名为.py的文件，包含要导入到程序中的代码。


def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) + "-用以下配料将披萨英寸:")
    for topping in toppings:
        print("- " + topping)
