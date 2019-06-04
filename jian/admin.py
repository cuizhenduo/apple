# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Winjian
# Register your models here.
class winJian(admin.ModelAdmin):
    list_display = ('title', 'time')

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js',
        )
'''
class sumJian(admin.ModelAdmin):
    list_display = ('title', 'time')

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js',
        )
'''
admin.site.register(Winjian,winJian)
#admin.site.register(Sumjian,sumJian)