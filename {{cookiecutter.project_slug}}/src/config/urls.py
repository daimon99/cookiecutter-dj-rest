"""tjccconfig URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import path, include
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from django.core.cache import cache
import logging
import sentry_sdk
from django_dj_plugin.utils import get_real_ip

log = logging.getLogger(__name__)

# 如果要对菜单排序，参考下面代码：

"""
def get_app_list(self, request):
    ordering = {
                "Event heros": 1,
                "Event villains": 2,
                "Epics": 3,
                "Events": 4
    }
    app_dict = self._build_app_dict(request)
    # a.sort(key=lambda x: b.index(x[0]))
    # Sort the apps alphabetically.
    app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
    # Sort the models alphabetically within each app.
    for app in app_list:
        app['models'].sort(key=lambda x: x['name'])
    return app_list
admin.get_app_list = get_app_list
"""


# @login_required(login_url='/admin/login')
def private_view(request: HttpRequest, path):
    user: User = request.user

    # 由于企业微信 / 微信 等环境，在打开附件时，需要用其它浏览器打开，因此会导致cookie失效。
    # 因此在user是anonymouse的时候，还需要再补充判断下临时token是否有效
    # 但是这里又带来另个问题，就是浏览器会劫持用户链接，从而多次下载此文件。这个问题如何解决，是个麻烦事
    # 为了安全考虑，还是禁用 download_token 比较好
    # 长远来看，应该弄一个提取码。非登录态用户用提取码来下载文件
    # 临时的办法，就是token配合ip一起来认证。只有允许的IP范围可以下载文件
    token = request.GET.get('download_token')

    def validate_token(token, ip):
        return True

    ip = get_real_ip(request)
    is_token_valid = validate_token(token, ip)
    if is_token_valid:
        log.warning('private_view, use token to download: %s, %s', path, token)
        return serve(request, path, document_root=settings.MEDIA_ROOT)
    elif user.has_module_perms('{{cookiecutter.project_slug}}'):
        log.warning("private_view, user have permission, now download file: %s, %s", user, path)
        return serve(request, path, document_root=settings.MEDIA_ROOT)
    else:
        log.warning("private_view, user have no permission: %s, %s", user, path)
        return HttpResponseForbidden()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('{{cookiecutter.project_slug}}/', include('{{cookiecutter.project_slug}}.urls')),
    path('api/v1/', include('{{cookiecutter.project_slug}}.urls_api_v1')),
    path('api/auth/', include('rest_framework.urls')),
    path('api/docs/', include_docs_urls(title='{{cookiecutter.project_name}}API', public=False)),
    path('api/auth-jwt/', obtain_jwt_token),  # POST email=email&password=password
    path('api/auth-jwt-verify/', verify_jwt_token),
    path('api/auth-jwt-refresh/', refresh_jwt_token),
    path(f'upload/<path:path>', private_view())
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
