# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Earth(models.Model):
    title = models.CharField('标题',max_length=200)
    article = models.TextField('文章')
    time = models.DateTimeField('时间', auto_now=True)
    class Meta:
        verbose_name = '土壤'
        verbose_name_plural = '土壤'
    def __unicode__(self):
        return self.title

class Shifei(models.Model):
    title = models.CharField('标题',max_length=200)
    article = models.TextField('文章')
    time = models.DateTimeField('时间', auto_now=True)
    class Meta:
        verbose_name = '施肥'
        verbose_name_plural = '施肥'
    def __unicode__(self):
        return self.title


class Water(models.Model):
    title = models.CharField('标题',max_length=200)
    article = models.TextField('文章')
    time = models.DateTimeField('时间', auto_now=True)
    class Meta:
        verbose_name = '灌水'
        verbose_name_plural = '灌水'
    def __unicode__(self):
        return self.title