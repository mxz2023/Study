from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("app2中的index方法")

def show_id(request,id):
    return HttpResponse("app2中的show_id方法,参数为id,值为"+str(id))

def show_uuid(request,id):
    return HttpResponse("app2中的show_uuid方法,参数为id,值为"+str(id))

def show_slug(request,q):
    return HttpResponse("app2中的show_slug方法,参数为q,值为"+str(q))

def article_list(request,year):
    return HttpResponse("app2中的article_list方法,参数为year,指定4位，值为"+str(year))

def article_page(request,page,key):
    return HttpResponse("app2中的article_page方法,参数为page,任意数字，值为"+str(page)+" 参数key，字母数字下划线，值为"+key)

