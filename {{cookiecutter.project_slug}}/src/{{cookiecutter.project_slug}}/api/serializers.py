# coding: utf-8
"""接口数据模型代码"""

from rest_framework import serializers

from {{cookiecutter.project_slug}} import models as m


# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = m.Project
#         fields = '__all__'
#
#
# class ContractSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = m.Project
#         fields = ['id', 'project']
#
#     project = ProjectSerializer()
