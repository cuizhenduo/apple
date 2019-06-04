# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Chong(models.Model):
    title = models.CharField('标题',max_length=200)
    article = models.TextField('文章')
    time = models.DateTimeField('时间', auto_now=True)
    class Meta:
        verbose_name = '虫害'
        verbose_name_plural = '虫害'
    def __unicode__(self):
        return self.title

class Bing(models.Model):
    title = models.CharField('标题',max_length=200)
    article = models.TextField('文章')
    time = models.DateTimeField('时间', auto_now=True)
    class Meta:
        verbose_name = '病害'
        verbose_name_plural = '病害'
    def __unicode__(self):
        return self.title


class Cao(models.Model):
    title = models.CharField('标题',max_length=200)
    article = models.TextField('文章')
    time = models.DateTimeField('时间', auto_now=True)
    class Meta:
        verbose_name = '草害'
        verbose_name_plural = '草害'
    def __unicode__(self):
        return self.title