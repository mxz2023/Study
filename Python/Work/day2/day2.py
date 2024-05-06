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
module.regist()
module.login()

# 通过包的方式实现登录注册功能
userRegist.regist()
userLogin.login()
