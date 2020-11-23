#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/23 10:43
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_8.4.1_functionModifyList.py
# @Software: PyCharm

# 将列表传递给函数后，函数可对其进行修改。
# 在函数中对这个列表所有的任何操作都是永久性的。


# 模拟不使用函数的情况下

# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # 模拟根据设计制作3D打印模型的过程
    print("打印模型: " + current_design)
    completed_models.append(current_design)
# 输出：
# 打印模型: dodecahedron
# 打印模型: robot pendant
# 打印模型: iphone case

# 显示打印好的所有模型
print("\n以下型号已经被打印出来:")
for completed_model in completed_models:
    print(completed_model)


# 输出：
# 以下型号已经被打印出来:
# dodecahedron
# robot pendant
# iphone case


# 模拟使用函数情况
def print_models(unprinted_designs, completed_models):
    """
    参数：
    unprinted_designs： 未打印出的设计， 列表类型
    completed_models： 打印完成的模型， 列表类型
    描述：
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # 模拟根据设计制作3D打印模型的过程
        print("打印模型: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """
    参数：
    completed_models：打印完成的模型，列表类型
    描述：
    显示打印好的所有模型
    """
    print("\n以下型号已经被打印出来:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 调用函数
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
# 输出：
# 以下型号已经被打印出来:
# dodecahedron
# robot pendant
# iphone case
