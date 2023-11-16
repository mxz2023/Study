# -*- coding: utf-8 -*-
"""
@Time ： 2023/11/15 09:06
@Auth ： 浮生半日闲
@File ： urls.py
@IDE ： PyCharm
@Motto：Code changes Everything

"""
from django.urls import path
from app6 import views

urlpatterns = [
    path('user_reg/', views.user_reg, name='user_reg'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('user_index/', views.user_index, name='user_index'),
    path('user_edit/', views.user_edit, name='user_edit'),
]
