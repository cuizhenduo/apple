# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class KindofEarly(models.Model):
    title = models.CharField('标题',max_length=200)
    article = models.TextField('文章')
    time = models.DateTimeField('时间', auto_now=True)
    class Meta:
        verbose_name = '主要品种-早熟'
        verbose_name_plural = '主要品种-早熟'
    def __unicode__(self):
        return self.title

class KindofMid(models.Model):
    title = models.CharField('标题',max_length=200)
    article = models.TextField('文章')
    time = models.DateTimeField('时间', auto_now=True)
    class Meta:
        verbose_name = '主要品种-中熟'
        verbose_name_plural = '主要品种-中熟'
    def __unicode__(self):
        return self.title

class KindofLate(models.Model):
    title = models.CharField('标题',max_length=200)
    article = models.TextField('文章')
    time = models.DateTimeField('时间', auto_now=True)
    class Meta:
        verbose_name = '主要品种-晚熟'
        verbose_name_plural = '主要品种-晚熟'
    def __unicode__(self):
        return self.title