from __future__ import unicode_literals
from django.db import models

# Create your models here.
class userinfo(models.Model):
    username = models.CharField('用户名',max_length=200)
    password = models.CharField('密码', max_length=200)
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'
    def __unicode__(self):
        return self.title