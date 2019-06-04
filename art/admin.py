# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import wenzhang
# Register your models here.
class Wenzhang(admin.ModelAdmin):
    list_display = ('title', 'time')

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js',
        )

admin.site.register(wenzhang,Wenzhang)


class MyAdminSite(admin.AdminSite):
    site_header = '苹果后台管理'  # 此处设置页面显示标题
    site_title = '苹果'  # 此处设置页面头部标题


admin_site = MyAdminSite(name='management')
admin.site.site_header = '苹果后台管理'
admin.site.site_title = '苹果'