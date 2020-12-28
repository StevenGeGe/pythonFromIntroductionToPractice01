#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/12/28 20:52
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_16-2-2_population.py
# @Software: PyCharm

# 绘制世界人口地图


import json

file_name = './data/population_json.json'

with open(file_name) as file_object:
    pop_data = json.load(file_object)

# 打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == '1965':
        country_name = pop_dict['Country Name']
        population = pop_dict['Value']
        print(country_name + "：" + population)
