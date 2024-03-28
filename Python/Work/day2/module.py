# -*- coding: utf-8 -*-
"""
@Time ： 2024/3/28 12:33
@Auth ： 浮生半日闲
@File ： module.py
@IDE ： PyCharm
@Motto：Code changes Everything

"""


# 注册功能的函数
def regist():
    while True:
        username = input('请输入注册的用户名:')

        has = False
        with open('userData.txt', 'r') as fpr:
            msg_list = fpr.readlines()
            for msg in msg_list:
                u_list = msg.split(':')
                uname = u_list[0]
                if username == uname:
                    print('用户名已经存在，请重新输入')
                    has = True
                    break
        if has:
            continue

        password = input('请输入注册的密码:')
        repeatPwd = input('请再次输入密码:')

        if password == repeatPwd:
            print('注册成功')
            # 将用户名和密码进行存储
            with open('userData.txt', 'a') as fpr:
                fpr.writelines([username + ':' + password + '\n'])

            break
        else:
            print('两次密码不一致：注册失败！')


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