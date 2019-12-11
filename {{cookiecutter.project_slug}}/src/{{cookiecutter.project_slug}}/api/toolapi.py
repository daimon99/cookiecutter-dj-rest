# coding: utf-8
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from telegraf.defaults.django import telegraf

from ..utils.logtools import TimeIt

from .. import models as m


class ToolsApi(viewsets.ViewSet):
    authentication_classes = ()
    permission_classes = ()

    @action(['get'], detail=False)
    def hello(self, req: Request):
        """Sample code
        """
        with TimeIt() as timeit:
            code = 0
        telegraf.metric('hello', {'duration': timeit.duration}, {'code': code})
        return Response({'code': code, 'msg': 'success'})
