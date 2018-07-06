# coding: utf-8
import coreapi
from django.db import connection
from rest_framework import serializers, viewsets, decorators
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from urllib import parse

from django.contrib.auth.models import User
from .. import models as m


class UserExtSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.UserExt
        fields = ('company',)


class UserSerializer(serializers.ModelSerializer):
    userext = UserExtSerializer(
        many=False,
        read_only=True,
    )

    class Meta:
        model = m.User
        fields = ('id', 'username', 'userext')


class UserApi(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    schema = CustomSchema()

    @decorators.action(['GET'], detail=False)
    def current(self, request):
        """返回当前登录的用户信息
        """
        user: User = request.user
        userext = request.user.userext if hasattr(request.user, 'userext') else None
        groups = [i.name for i in user.groups.all()]
        return Response({'code': 0, 'message': '调用成功', 'data': {
            'id': user.id,
            'username': user.username,
            'tel': '',
            'role': groups
        }})

    @decorators.action(['POST'], detail=False)
    def logout(self, request):
        """登出。
        注销该用户使用的资源
        """
        user: User = request.user
        return Response({
            'code': 0, 'message': '登出成功'
        })


