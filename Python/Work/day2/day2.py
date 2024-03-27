# -*- coding: utf-8 -*-
"""
@Time ： 2024/3/27 23:16
@Auth ： 浮生半日闲
@File ： day2.py
@IDE ： PyCharm
@Motto：Code changes Everything

"""

filename = 'hello world.txt'

fp = open(filename, 'w')
fp.write('hello bobo')
fp.close()  # 将文件内容清空，在写入新数据
