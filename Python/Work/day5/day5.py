# -*- coding: utf-8 -*-
"""
@Time ： 2024/4/10 20:53
@Auth ： 浮生半日闲
@File ： day5.py
@IDE ： PyCharm
@Motto：Code changes Everything

"""

import requests

url = 'http://www.baidu.com'
response = requests.get(url)
# response.encoding = 'utf-8'
response.encoding = 'gbk'

page_text = response.text


with open('baidu.html', 'w') as fp:
    fp.write(page_text)