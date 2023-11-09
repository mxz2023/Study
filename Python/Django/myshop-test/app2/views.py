from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
# /app2/index
def index(request):
    return HttpResponse("app2中的index方法")

def url_reverse(request):
    #使用reverse方法反向解析
    print("views函数中使用reverse解析的结果："+reverse("app2_url_reverse"))
    return render(request,"2/url_reverse.html")

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

# /app2/test_get
def test_get(request):
    print(request.get_host()) #域名+端口
    print(request.get_raw_uri()) #全部路径，包含参数
    print(request.path) #获取访问文件路径，不含参数
    print(request.get_full_path())#获取访问文件路径，包含参数
    print(request.method) #获取请求中的使用的HTTP方式(POST/GET)
    print(request.GET) #获取GET请求的参数
    print(request.META["HTTP_USER_AGENT"]) #用户浏览器的user-agent字符串
    print(request.META["REMOTE_ADDR"]) #客户端IP
    print(request.GET.get('username'))#获取get参数
    return HttpResponse("")

# /app2/test_post/
def test_post(request):
    print(request.method) #获取请求中的使用的HTTP方式(POST/GET)
    print(request.POST.get('username'))
    return render(request,'2/test_post.html')


# /app2/test_response/
def test_response(request):
    response=HttpResponse()
    response.write("hello django")
    response.write("<br>")
    response.write(response.content)
    response.write("<br>")
    response.write(response['Content-type'])
    response.write("<br>")
    response.write(response.status_code)
    response.write("<br>")
    response.write(response.charset)
    response.write("<br>")
    return response


# /app2/test_render/
def test_render(request):
    return render(request,'2/test_render.html',{'info':'hello django'},content_type='text/html')

def test_redirect(request):
    return redirect("https://www.phei.com.cn/")




