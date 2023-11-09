from django.urls import path, re_path
from app2 import views

urlpatterns = [
    path('index/',views.index, name='app2_index'),
    path('url_reverse/',views.url_reverse,name='app2_url_reverse'),

    path('show/<int:id>/',views.show_id,name='show_id'),
    path('article/<uuid:id>/',views.show_uuid,name='show_uuid'),
    path('article/<slug:q>/',views.show_slug,name='show_slug'),

    re_path(r'list/(?P<year>\d{4})/', views.article_list),
    re_path(r'page/(?P<page>\d+)&key=(?P<key>\w+)',views.article_page,name="article_page"),

]
