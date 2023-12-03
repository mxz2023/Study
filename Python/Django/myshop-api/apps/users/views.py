from django.shortcuts import render
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from apps.users.models import MyUser
from apps.users.serializer import MyUserRegSerializer, MyUserUpdateSerializer

from common.custommodelviewset import CustomModelViewSet

from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions


# Create your views here.
class MyUserViewSet(CustomModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserRegSerializer

    authentication_classes = (JWTTokenUserAuthentication, SessionAuthentication)

    def get_serializer_class(self):
        if self.action == "create":
            return MyUserRegSerializer
        elif self.action == "retrieve":
            return MyUserUpdateSerializer
        elif self.action == "update":
            return MyUserUpdateSerializer

        return MyUserUpdateSerializer

    def get_permissions(self):
        if self.action == "retrieve":
            print("retrieve")
            return [permissions.IsAuthenticated()]
        elif self.action == "update":
            print("update")
            return [permissions.IsAuthenticated()]
        else:
            return []

    # 获取当前用户
    def get_object(self):
        return self.request.user


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            myuser = MyUser.objects.get(Q(username=username) | Q(mobile=username))
            if myuser.check_password(password):
                return myuser
        except Exception as e:
            print('%s', e)
            return None
