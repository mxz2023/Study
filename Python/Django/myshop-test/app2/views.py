from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
# /app2/index
def index(request):
    return HttpResponse("app2中的index方法")

def url_reverse(request):
    #使用reverse方法反向解析
    print("views函数中使用reverse解析的结果："+reverse("app2_url_reverse"))
    return render(request,"1/index.html")

# /app2/show/1
def show_id(request,id):
    return HttpResponse("app2中的show_id方法,参数为id,值为"+str(id))

# /app2/artcle/00000000-0000-0000-0000-000000000000
def show_uuid(request,id):
    return HttpResponse("app2中的show_uuid方法,参数为id,值为"+str(id))

# /app2/artcle/abc123
def show_slug(request,q):
    return HttpResponse("app2中的show_slug方法,参数为q,值为"+str(q))

# /app2/list/2023
def article_list(request,year):
    return HttpResponse("app2中的article_list方法,参数为year,指定4位，值为"+str(year))

# /app2/list/page/10&key=test
def article_page(request,page,key):
    return HttpResponse("app2中的article_page方法,参数为page,任意数字，值为"+str(page)+" 参数key，字母数字下划线，值为"+key)

