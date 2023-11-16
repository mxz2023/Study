from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse
from app6.models import MyUser


# Create your views here.
def user_reg(request):
    if request.method == "GET":
        return render(request, '6/user_reg.html')
    if request.method == "POST":
        uname = request.POST.get("username", '')
        pwd = request.POST.get("password", '')
        if MyUser.objects.filter(username=uname):
            info = '用户已经存在'
        else:
            d = dict(username=uname, password=pwd, email='111@111.com', is_staff=1, is_active=1, is_superuser=1)
            user = MyUser.objects.create_user(**d)
            info = '注册成功,请登陆'
            # 跳转到登陆页面
            return redirect(reverse("user_login"))
        return render(request, '6/user_reg.html', {"info": info})


def user_login(request):
    if request.method == "GET":
        return render(request, '6/user_login.html')
    if request.method == "POST":
        uname = request.POST.get("username", '')
        pwd = request.POST.get("password", '')
        if MyUser.objects.filter(username=uname):  # 判断用户是否存在
            # 如果存在，进行验证
            user = authenticate(username=uname, password=pwd)
            if user:  # 如果验证通过
                if user.is_active:  # 如果用户状态为激活
                    login(request, user)  # 进行登陆操作，完成session的设置
                    return redirect(reverse("user_index"))
                else:
                    info = "用户还未激活"
            else:
                info = "账号密码不对，请重新输入"
        else:
            info = '用户账号不存在，请查询'
        return render(request, '6/user_login.html', {"info": info})


def user_logout(request):
    logout(request)
    return redirect(reverse("user_login"))


@permission_required("app6.view_user")
@login_required
def user_index(request):
    users = MyUser.objects.all()
    return render(request, '6/user_index.html', {"users": users})


@permission_required("app6.change_user")
@login_required
def user_edit(request):
    return render(request, '6/user_edit.html')


def test(request):
    return HttpResponse("我也执行了")


