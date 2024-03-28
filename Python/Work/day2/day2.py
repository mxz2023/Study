# -*- coding: utf-8 -*-
"""
@Time ： 2024/3/27 23:16
@Auth ： 浮生半日闲
@File ： day2.py
@IDE ： PyCharm
@Motto：Code changes Everything

"""

import module
import user.regist as userRegist
import user.login as userLogin

filename = 'hello world.txt'

fp = open(filename, 'w')
fp.write('hello mxz')
fp.close()  # 将文件内容清空，在写入新数据

fp = open(filename, 'a')
fp.write('hello bobo')
fp.close()  # 在文件数据末尾追加数据

with open(filename, 'r') as fp:  # fp = open()
    text = fp.read(5)
print(text)

# 上下两组代码功效一样
fp = open(filename, 'r')
text = fp.read(5)
fp.close()
print(text)


# 实现一个图片的复制粘贴功能
# 原理：将图片文件打开，读取图片文件中二进制的数据，将二进制数据写入到另一个文件即可

def cvImg(imgPath, targetPath):
    # imgPath是原图文件路径
    # targetPath粘贴路径

    # 打开原图
    with open(imgPath, 'rb') as fp1:
        # 读取图片数据
        img_data = fp1.read()

    with open(targetPath, 'wb') as fp2:
        fp2.write(img_data)


cvImg('./IMG_1504.jpeg', './IMG_1504_NEW.jpeg')

'''
简易登录注册：
    注册：用户从键盘上录入注册的用户名、密码和重复密码，如果两次密码一致的表示
         注册成功，将注册的用户名和密码保存到文件中进行存储。
    登录：用户录入登录的用户名和密码，然后程序需要校验改组用户名和密码是否之前
         被注册过，如果是，则登录成功，否则登录失败。
'''

# 通过模块的方式实现登录注册功能
# module.regist()
# module.login()

# 通过包的方式实现登录注册功能
# userRegist.regist()
# userLogin.login()

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
