# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import BloTime,Tie,UnTie,Collect
# Register your models here.
class bloTime(admin.ModelAdmin):
    list_display = ('title', 'time')

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js',
        )

class tie(admin.ModelAdmin):
    list_display = ('title', 'time')

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js',
        )

class unTie(admin.ModelAdmin):
    list_display = ('title', 'time')

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js',
        )

class collect(admin.ModelAdmin):
    list_display = ('title', 'time')

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js',
        )
admin.site.register(BloTime,bloTime)
admin.site.register(Tie,tie)
admin.site.register(UnTie,unTie)
admin.site.register(Collect,collect)
