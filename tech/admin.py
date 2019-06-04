# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import KindofEarly,KindofMid,KindofLate
# Register your models here.
class kindofEarly(admin.ModelAdmin):
    list_display = ('title', 'time')

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js',
        )

class kindofMid(admin.ModelAdmin):
    list_display = ('title', 'time')

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js',
        )

class kindofLate(admin.ModelAdmin):
    list_display = ('title', 'time')

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js',
        )

admin.site.register(KindofEarly,kindofEarly)
admin.site.register(KindofMid,kindofMid)
admin.site.register(KindofLate,kindofLate)