#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2020/11/12 15:06
# @Author  : Yong
# @Email   : Yong_GJ@163.com
# @File    : task_4_diff.py
# @Software: PyCharm


import xlrd
import openpyxl
import time

a = [1, 2, 3]
b = [2, 3, 4, 5]
inter = [i for i in b if i not in a]
print(inter)

workbook_name_more = "C:\\Users\Yong_\Desktop\\tmp\huifang\202010智能回访数据.xlsx"
workbook_name_les = "C:\\Users\Yong_\Desktop\\tmp\huifang\结案-202010.xlsx"

jin_ke_cols = \
    xlrd.open_workbook(r'C:\Users\Yong_\Desktop\tmp\huifang\202010智能回访数据.xlsx'). \
        sheet_by_name('Select t_callsnap'). \
        col_values(0)

hy_cols = \
    xlrd.open_workbook(r'C:\Users\Yong_\Desktop\tmp\huifang\结案-202010.xlsx'). \
        sheet_by_name('SQL Results'). \
        col_values(1)
print('金科：', end="")
print(len(jin_ke_cols))
print('浩宜：', end="")
print(len(hy_cols))
print('初始对比：', end="")
print(len(hy_cols) - len(jin_ke_cols))

print('开始对比：' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
inter = [i for i in hy_cols if i not in jin_ke_cols]
print('结束对比：' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# inter.sort()
print('对比结果：', end="")
print(len(inter))

result = open('C:\\Users\Yong_\Desktop\\tmp\huifang\data.xls', 'w', encoding='gbk')
result.write('保单号\t\n')
for i in range(len(inter)):
    result.write(str(inter[i]) + '\t')
    result.write('\n')
result.close()
print('结束时间：' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
