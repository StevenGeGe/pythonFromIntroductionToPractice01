#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/12/10 20:47
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_16-1-5_datetime.py
# @Software: PyCharm

# 时间日期模块

# datetime.strptime('2020-12-10', '%Y-%m-%d')： 格式化日期
from datetime import datetime

first_date = datetime.strptime('2020-12-10', '%Y-%m-%d')
print(first_date)
