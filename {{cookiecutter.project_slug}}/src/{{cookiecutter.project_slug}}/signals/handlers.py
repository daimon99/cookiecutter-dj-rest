# coding: utf-8
import logging

from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import Company, UserExt

log = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def save_user(sender, instance: User, created, **kwargs):
    if not created:
        return
    log.warning('新建用户：%s', instance)
