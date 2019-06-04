# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class wenzhang(models.Model):
    title = models.CharField('标题',max_length=200)
    article = models.TextField('文章')
    time = models.DateTimeField('时间', auto_now=True)
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
    def __unicode__(self):
        return self.title