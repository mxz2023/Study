# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app6.models import MyUser

admin.site.register(MyUser, UserAdmin)


