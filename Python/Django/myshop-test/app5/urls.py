# -*- coding: utf-8 -*-
"""
@Time ： 2023/11/14 23:17
@Auth ： 浮生半日闲
@File ： urls.py
@IDE ： PyCharm
@Motto：Code changes Everything

"""

from django.urls import path
from app5 import views


urlpatterns = [
    path('upload_file/', views.upload_file),
    path('userinfoform/', views.userinfo_form),
    path('userinfomsgform/', views.userinfo_msg_form),
]
