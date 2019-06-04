# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Earth,Shifei,Water
# Register your models here.
class earth(admin.ModelAdmin):
    list_display = ('title','time')

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js',
        )

class shifei(admin.ModelAdmin):
    list_display = ('title','time')

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js',
        )

class water(admin.ModelAdmin):
    list_display = ('title', 'time')

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js',
        )

admin.site.register(Earth,earth)
admin.site.register(Shifei,shifei)
admin.site.register(Water,water)