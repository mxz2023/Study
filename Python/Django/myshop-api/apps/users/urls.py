# -*- coding: utf-8 -*-
"""
@Time ： 2023/11/24 07:25
@Auth ： 浮生半日闲
@File ： urls.py
@IDE ： PyCharm
@Motto：Code changes Everything

"""
from django.urls import path, include, re_path
from apps.users import views

user_list = views.MyUserViewSet.as_view({
    'get': 'retrieve',
    'post': 'create',
})

user_detail = views.MyUserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('users/', user_list),
    path('users/<pk>/', user_detail),  # 查找、更新、删除
]
