# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BloTime(models.Model):
    title = models.CharField('标题',max_length=200)
    article = models.TextField('文章')
    time = models.DateTimeField('时间', auto_now=True)
    class Meta:
        verbose_name = '花期'
        verbose_name_plural = '花期'
    def __unicode__(self):
        return self.title

class Tie(models.Model):
    title = models.CharField('标题',max_length=200)
    article = models.TextField('文章')
    time = models.DateTimeField('时间', auto_now=True)
    class Meta:
        verbose_name = '套袋'
        verbose_name_plural = '套袋'
    def __unicode__(self):
        return self.title

class UnTie(models.Model):
    title = models.CharField('标题',max_length=200)
    article = models.TextField('文章')
    time = models.DateTimeField('时间', auto_now=True)
    class Meta:
        verbose_name = '解袋'
        verbose_name_plural = '解袋'
    def __unicode__(self):
        return self.title


class Collect(models.Model):
    title = models.CharField('标题',max_length=200)
    article = models.TextField('文章')
    time = models.DateTimeField('时间', auto_now=True)
    class Meta:
        verbose_name = '采收'
        verbose_name_plural = '采收'
    def __unicode__(self):
        return self.title