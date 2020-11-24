#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/24 19:14
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_9.1.1_class.py
# @Software: PyCharm

# 面向对象编程
# 基于类创建对象对 时，每个对象都自动具备这种通用行为，然后可根据需要赋予每个对象独特的个性
# 根据类来创建对象被称为实例化

# 类中，
#   1、类中的函数称为方法
#   2、__init__：是一个特殊的方法， 没当创建一个类的实例是，会自动执行此方法。
#       开头和结尾各有两个下划线，这是约定，避免python默认方法与普通方法发生名称冲突。
#   3、形参self ，必须位于其他形参的前面，python创建实例时，会自动传入实参self。
#      每个与类相关联的方法调用都自动传递实参self，
#      他是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
#   4、只需要给其他需要的参数即可，self会自动传入。
#   5、python2.7中创建类时，需要在括号内包含单词object。
#       class ClassName(object):
#       --snip--
#   6、python3中，类中的括号，可以要也可以不要
#       class ClassName:
#       class ClassName():
#   7、大写的为类名， 小写的为实例名
#       my_dog = Dog('willie', 6)
#   8、类中的方法通过(实例名.方法名()) 来调用


class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
        print("Dog类 初始化 " + name + " " + str(age))

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " 正在蹲下.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " 在打滚!")


my_dog = Dog('willie', 6)

print("狗狗的名字是 " + my_dog.name.title())
print("狗狗的年龄是 " + str(my_dog.age) + "岁")

# 调用类中的方法
my_dog.sit()
my_dog.roll_over()

# 创建多个实例
your_dog = Dog('小明', 9)
