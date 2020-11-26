#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/26 19:37
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_10.2.3_writeFileAdditional.py
# @Software: PyCharm

# 附加模式写入文件
# 不覆盖源文件内容情况下，打开文件，并在末尾追加；
# 如果文件不存在，则会创建
# 如果文件末尾是空行，则删除一个空行，在后面追加。

file_name = 'programming.txt'

with open(file_name, 'a', encoding='utf-8') as file_object:
    file_object.write('i love 七月.\n')
    file_object.write('i love 8月.')
