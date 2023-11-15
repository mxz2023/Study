# -*- coding: utf-8 -*-
"""
@Time ： 2023/11/14 23:29
@Auth ： 浮生半日闲
@File ： forms.py
@IDE ： PyCharm
@Motto：Code changes Everything

"""

from django import forms
from django.core.exceptions import ValidationError
import re


def age_validate(value):
    if value < 1 or value > 120:
        raise ValidationError('年龄范围为1-120岁')


def mobile_validate(value):
    mobile_re = re.compile(
        r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')


class UserInfoForm(forms.Form):
    """用户状态"""
    STATUS = ((None, '请选择'), (0, '正常'), (1, '无效'),)
    username = forms.CharField(label="用户名", min_length=6,
                               widget=forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': "请输入用户名"}))
    password = forms.CharField(label="密码", min_length=6, max_length=10,
                               widget=forms.widgets.PasswordInput(attrs={"class": "password"}, render_value=True))
    age = forms.IntegerField(label="年龄", initial=1)
    mobile = forms.CharField(label="手机号码")
    status = forms.ChoiceField(label="用户状态", choices=STATUS)
    createdate = forms.DateTimeField(label="创建时间", required=False)


class UserBaseInfoForm(forms.Form):
    """用户状态"""
    STATUS = ((None, '请选择'), (0, '正常'), (1, '无效'),)
    username = forms.CharField(label="用户名", min_length=6,
                               error_messages={
                                   'required': '用户姓名不能为空',
                                   'min_length': '长度最少6位',
                                   'invalid': '输入正确的用户姓名'
                               })
    age = forms.IntegerField(label="年龄", initial=1, validators=[age_validate],
                             error_messages={
        'required': '年龄不能为空',
    })
    status = forms.ChoiceField(label="用户状态", choices=STATUS,
                               error_messages={
                                   'required': '用户状态不能为空',
                               })
    createdate = forms.DateTimeField(label="创建时间", required=False)


class UserInfoMsgForm(forms.Form):
    """用户状态"""
    STATUS = ((None, '请选择'), (0, '正常'), (1, '无效'),)
    username = forms.CharField(label="用户名", min_length=6,
                               widget=forms.widgets.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': "请输入用户名"}),
                               error_messages={
                                   'required': '用户姓名不能为空',
                                   'min_length': '长度最少6位',
                                   'invalid': '输入正确的用户姓名'
                               })
    password = forms.CharField(label="密码", min_length=6, max_length=10,
                               widget=forms.widgets.PasswordInput(
                                   attrs={"class": "password"}, render_value=True),
                               error_messages={
                                   'max_length': '密码最长10位',
                                   'required': '密码不能为空',
                                   'min_length': '密码最少6位'
                               })
    age = forms.IntegerField(label="年龄", initial=1, validators=[age_validate],
                             error_messages={
        'required': '年龄不能为空',
    })
    mobile = forms.CharField(label="手机号码", validators=[mobile_validate],
                             error_messages={
        'required': '手机号码不能为空',
    })
    status = forms.ChoiceField(label="用户状态", choices=STATUS,
                               error_messages={
                                   'required': '用户状态不能为空',
                               })
    createdate = forms.DateTimeField(label="创建时间", required=False)


