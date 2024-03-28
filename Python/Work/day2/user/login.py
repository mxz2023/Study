# -*- coding: utf-8 -*-
"""
@Time ： 2024/3/28 12:40
@Auth ： 浮生半日闲
@File ： login.py
@IDE ： PyCharm
@Motto：Code changes Everything

"""


# 登录功能的函数
def login():
    username = input('请输入登录的用户名:')
    password = input('请输入登录的密码:')
    state = False  # 保存判定登录的状态（False表示登录失败，True表示登录成功）
    # 判定登录状态
    with open('userData.txt', 'r') as fpr:
        msg_list = fpr.readlines()  # ['bobo:123\n', 'jay:456\n']
        for msg in msg_list:
            u_list = msg.split(':')
            uname = u_list[0]
            pwd = u_list[1].strip()
            if username == uname and password == pwd:
                state = True
                break
        if not state:
            print('登录失败：用户名密码不正确')
        else:
            print('登录成功！')
