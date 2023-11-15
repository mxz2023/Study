import os

from django.shortcuts import render
from django.http import HttpResponse
from .forms import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def upload_file(request):
    if request.method == "GET":
        return render(request, "5/upload.html")
    # 请求方法为POST时，进行处理。文件上传为POST请求。
    if request.method == "POST":
        # 获取上传的文件，如果没有文件，则默认为None
        myFile = request.FILES.get("myfile", None)
        if myFile:
            # 二进制的写操作
            path = 'media/uploads/'
            if not os.path.exists(path):
                os.makedirs(path)
            dest = open(os.path.join(path+myFile.name),'wb+')
            for chunk in myFile.chunks():      # 分块写入文件
                dest.write(chunk)
            dest.close()
            return HttpResponse("上传完成!")
        else:
            return HttpResponse("没有上传文件！")


def userinfo_form(request):
    if request.method == "GET":
        myform = UserInfoForm()
        return render(request, "5/userinfo.html", {'form_obj': myform})


def userinfo_msg_form(request):
    if request.method == "GET":
        myform = UserInfoMsgForm()
        return render(request, "5/userinfoform.html", {'form_obj': myform})
    else:
        f = UserInfoMsgForm(request.POST)
        if f.is_valid():
            print(f.clean())
            print(f.cleaned_data["username"])
            print(f.data)
        else:
            errors = f.errors
            print(errors)
            return render(request, "5/userinfoform.html", {'form_obj': f, 'errors': errors})
        return render(request, "5/userinfoform.html", {'form_obj': f})



