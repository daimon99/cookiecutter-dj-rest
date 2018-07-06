from django.db import models
from django_extensions.db.models import TimeStampedModel

from django.contrib.auth.models import User


# Create your models here.


class Company(TimeStampedModel):
    class Meta:
        verbose_name = verbose_name_plural = '01 - 公司列表'

    name = models.CharField(max_length=128, blank=True, null=True, help_text='公司名称')

    def __str__(self):
        return f'{self.id}-{self.name}'


class UserExt(TimeStampedModel):
    """用户与公司关系表。包括用户的扩展属性。"""

    class Meta:
        verbose_name = verbose_name_plural = '03 - 座席用户'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return f'{self.id}-{self.name}'
