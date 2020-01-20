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
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from django.conf import settings

admin.site.site_header = '{{cookiecutter.project_name}}'
admin.site.site_title = '{{cookiecutter.project_name}}'
admin.site.index_title = '首页'
admin.site.site_url = None

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('{{cookiecutter.project_slug}}.urls_api_v1')),
    path('api/auth/', include('rest_framework.urls')),
    path('api/docs/', include_docs_urls(title='{{cookiecutter.project_name}}API', public=False)),
    path('api/auth-jwt/', obtain_jwt_token),  # POST email=email&password=password
    path('api/auth-jwt-verify/', verify_jwt_token),
    path('api/auth-jwt-refresh/', refresh_jwt_token),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),

                      # For django versions before 2.0:
                      # url(r'^__debug__/', include(debug_toolbar.urls)),

                  ] + urlpatterns
