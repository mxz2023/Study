# -*- coding: utf-8 -*-
"""
@Time ： 2024/3/28 12:40
@Auth ： 浮生半日闲
@File ： regist.py
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
