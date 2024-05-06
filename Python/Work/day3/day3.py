# -*- coding: utf-8 -*-
"""
@Time ： 2024/4/1 22:14
@Auth ： 浮生半日闲
@File ： day3.py
@IDE ： PyCharm
@Motto：Code changes Everything

"""
# 正则表达式
"""
单字符：
    . : 除换行以外所有字符
    [] ：[aoe] [a-w] 匹配集合中任意一个字符
    \d ：数字  [0-9]
数量修饰：
    * : 任意多次  >=0
    + : 至少1次   >=1
    ? : 可有可无  0次或者1次
    {m} ：固定m次 hello{3,}
    {m,} ：至少m次
    {m,n} ：m-n次
边界：
    $ : 以某某结尾 
    ^ : 以某某开头
分组：
	(ab)  
贪婪模式： .*
非贪婪（惰性）模式： .*?
"""

import re

# 提取170
string = '我喜欢身高为170的女孩'
ex = '\d+'
result = re.findall(ex, string)
print(result)
#####################################################################
# 提取出http://和https://
key = 'http://www.baidu.com and https://boob.com'
ex = 'https?://'
result = re.findall(ex, key)
print(result)
#####################################################################

# 提取出hello
key = 'lalala<hTml>hello</HtMl>hahah'  # 输出<hTml>hello</HtMl>
ex = '<hTml>.*</HtMl>'
result = re.findall(ex, key)
print(result)

#####################################################################
# 提取出hit.
key = 'bobo@hit.edu.com'  # 想要匹配到hit.
# ex = 'h.*\.' #贪婪模式
ex = 'h.*?\.'  # ？将正则的贪婪模式调整为非贪婪模式。默认下为贪婪模式
result = re.findall(ex, key)
print(result)
#####################################################################
# 匹配sas和saas
key = 'saas and sas and saaas'
ex = 'sa{1,2}s'
result = re.findall(ex, key)
print(result)
#####################################################################
key = '你好我的手机号是13222222222你记住了吗'
ex = '1[3,5,7,8,9]\d{9}'
result = re.findall(ex, key)
print(result)

# ？将贪婪模式调整为非贪婪模式
# +？和*？的区别在于+？至少匹配一个，*？可以匹配0个
key = 'aaaabb,aaabbb,aaabbbb,ab,b'

print("+?")
ex1 = '[a+?]b'
result1 = re.findall(ex1, key)
print(result1)  #

ex2 = 'a[b+?]'
result2 = re.findall(ex2, key)
print(result2)

ex3 = 'ab+?'
result3 = re.findall(ex3, key)
print(result3)

ex4 = 'a+?b'
result4 = re.findall(ex4, key)
print(result4)

print("*?")

ex1 = '[a*?]b'
result1 = re.findall(ex1, key)
print(result1)  #

ex2 = 'a[b*?]'
result2 = re.findall(ex2, key)
print(result2)

ex3 = 'ab*?'
result3 = re.findall(ex3, key)
print(result3)

key = 'xaaacabb,xaaaebbb,xaaabbbb,ab,b,cb, xb'
ex4 = 'xa+.b'
result4 = re.findall(ex4, key)
print(result4)

# 异常处理
try:
    # 1 / 0
    print("hello world")
except ZeroDivisionError as e:
    print(e)

except Exception as e:
    print(e)

else:
    print("没有发生异常")

finally:
    print("都会执行")

# 推导式

# 列表推导式
alist = [x ** 2 for x in range(1, 10) if x % 2 == 0]
print(alist)

# 多重循环
alist = [a + b for a in "123" for b in "abc"]
print(alist)

# 字典推导式
dic = {x: x ** 2 for x in [2, 4, 6]}
print(dic)

# 集合推导式
a = {x for x in 'aabbccddeeff'}
print(a)

# Excel
# 如何将数据存储到Excel文件中
# 1.在程序中人为创建一个数据表格
# 如何将数据存储到Excel文件中
import pandas as pd  # DataFrame的数据结构（程序中的表格）
import numpy as np

# 爬取的是员工的薪资数据
table = pd.DataFrame(columns=['name', 'salary'])  # 创建一个数据表格
# 进行行的添加使用的loc的机制
table.loc[0] = ['Bobo', 3000]
table.loc[1] = ['Jay', 5000]
print(table)
# 将数据表格存储到Excel
table.to_excel('data.xlsx')

# 如何将Excel文件中的内容读取到程序中
# 将文件的数据读取到程序中
# dfPhone = pd.read_excel('Phone.xlsx', index_col=0)
# print(dfPhone)

# 查看其属性、概览和统计信息
# print("显示头部10行")
# print(dfPhone.head(10))  # 显示头部10行，默认5个
# print("显示末尾10行")
# print(dfPhone.tail(10))  # 显示末尾10行，默认5个
# print("====================================")
# print(dfPhone.describe())  # 查看数值型列的汇总统计,计数、平均值、标准差、最小值、四分位数、最大值
# print("====================================")
# print(dfPhone.info())  # 查看列索引、数据类型、非空计数和内存信息

# 创建一个数据表格
df = pd.DataFrame(data=[[1, 2, 6], [3, 4, 8]], index=('A', 'B'), columns=['a', 'b', 'c'])
print("打印表格")
print(df)
print("打印表格的a列")
print(df['a'])  # 根据列索引访问指定的列
print("打印表格的B行")
print(df.loc['B'])  # 根据行索引访问行
print("打印表格的第一行")
print(df[0:1])  # 根据切片访问行数据
print("打印表格的a列到b列")
print(df.loc[:, 'a':'b'])  # 根据切片访问列数据

df = pd.DataFrame(data=np.random.randint(0, 100, size=(20, 3)),
                  index=list('ABCDEFHIJKLMNOPQRSTU'),
                  columns=['Python', 'Tensorflow', 'Keras'])
df.count()  # 非NAN值的数量
df.max(axis=0)  # 轴0最大值，即每一列最大值
df.min()  # 默认计算轴0最小值
df.median()  # 中位数
df.sum()  # 求和
df.mean(axis=1)  # 轴1平均值，即每一行的平均值
df.cumsum()  # 累加
df.cumprod()  # 累乘
df.std()  # 标准差
df.var()  # 方差
df.quantile(q=[0.2, 0.4, 0.8])  # 分位数
df['Python'].rank()  # 对序列中的元素值排名，该函数的返回值的也是一个序列，包含了原序列中每个元素值的名次。如果序列中包含两个相同的的元素值，那么会为其分配两者的平均排名
print(df)

df = pd.DataFrame({'item': ['Apple', 'Banana', 'Orange', 'Banana', 'Orange', 'Apple'],
                   'price': [4, 3, 3, 2.5, 4, 2],
                   # 'color': ['red', 'yellow', 'yellow', 'green', 'green', 'green'],
                   'weight': [12, 20, 50, 30, 20, 44]})

print(df)
# 计算每种水果的平均价格
print(df.groupby(by='item').groups)  # groups返回分组结果
print(df.groupby(by='item').mean())  # mean聚合操作只会对数值型的数据进行聚合
print(df.groupby(by='item').mean()['price'])
#
# # 聚合推荐方式
# mean_price_s = df.groupby(by='item')['price'].mean()
# print(mean_price_s)
# # 将每种水果的平均价格汇总到源数据中
# dic = mean_price_s.to_dict()
# df['mean_price'] = df['item'].map(dic)
# print(df)