# -*- coding: utf-8 -*-
"""
@Time ： 2023/11/16 09:17
@Auth ： 浮生半日闲
@File ： permmiddleware.py
@IDE ： PyCharm
@Motto：Code changes Everything

"""
from django.shortcuts import HttpResponse, render, redirect
from django.utils.deprecation import MiddlewareMixin
import re


class PermissionMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        # 获取当前路径
        curr_path = request.path
        print(curr_path)

        # 白名单处理
        white_list = ["/user_login/", "/user_reg/"]
        for w in white_list:
            if re.search(w, curr_path):
                return None  # 通过

        # 验证是否登陆
        # print(request.user.is_authenticated)
        if not request.user.is_authenticated:
            return redirect("/app6/user_login/")

        # 这里还可以继续处理一些权限细节，不在展开
        # 比如晚上12点以后关闭商城


