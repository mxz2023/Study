# -*- coding: utf-8 -*-
"""
@Time ： 2023/11/21 23:51
@Auth ： 浮生半日闲
@File ： urls.py
@IDE ： PyCharm
@Motto：Code changes Everything

"""
from django.urls import path, re_path
from apps.users import views

urlpatterns = [
    path('user_reg/', views.user_reg),
    path('user_login/', views.user_login),
    path('ajax_login_data/', views.ajax_login_data),
]
