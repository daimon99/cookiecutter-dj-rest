# coding: utf-8

# https://github.com/lukasvinclav/django-admin-numeric-filter
from admin_numeric_filter.admin import RangeNumericFilter, NumericFilterModelAdmin

from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import render

from . import models as m

admin.site.site_header = '{{cookiecutter.project_name}}'
admin.site.site_title = '{{cookiecutter.project_name}}'
admin.site.index_title = '首页'
admin.site.site_url = None

# Register your models here.

# sample admin
"""

@admin.register(m.Customer)
class CustomerAdmin(admin.NumericFilterModelAdmin):
    list_display = ('id', 'project', 'name', 'mobile_enc', 'task_name', 'created', 'modified')
    actions = ('do_uni_update_info', 'do_make_call', 'assign_task')
    list_select_related = ('task',)
    autocomplete_fields = ('project', 'task')
    search_fields = ('name', 'mobile_enc', 'project__name', 'task__name')
    ordering = ('id', )
    list_filter = (('id', RangeNumericFilter))

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        else:
            try:
                company = request.user.userext.company
                return m.Customer.objects.filter(project__company=company)
            except ObjectDoesNotExist:
                return m.Customer.objects.none()

    def assign_task(self, req, qs):
        user = req.user
        company = user.userext.company
        task_list = list(m.Task.objects.filter(assign_to__userext__company=company).all())
        customer_list = list(qs)

        if 'apply' in req.POST:
            task_id = req.POST.get('task_id')
            if not task_id:
                self.message_user(req, '没选择项目')
                return
            else:
                task = m.Task.objects.get(pk=task_id)
                qs.update(task_id=task_id)
                customerbiz.refresh_task(task)
                self.message_user(req, f"分配到任务成功：{task_id}")
                return
        return render(req, 'admin/customer/assign_task.html', context={'tasks': task_list, 'customers': customer_list})

    assign_task.short_description = '分配任务'
"""


