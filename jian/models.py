# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Winjian(models.Model):
    title = models.CharField('标题',max_length=200)
    article = models.TextField('文章')
    time = models.DateTimeField('时间', auto_now=True)
    class Meta:
        verbose_name = '剪枝'
        verbose_name_plural = '剪枝'
    def __unicode__(self):
        return self.title
'''
class Sumjian(models.Model):
    title = models.CharField('标题',max_length=200)
    article = models.TextField('文章')
    time = models.DateTimeField('时间', auto_now=True)
    class Meta:
        verbose_name = '夏剪'
        verbose_name_plural = '夏剪'
    def __unicode__(self):
        return self.title
'''