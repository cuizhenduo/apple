# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Machine
# Register your models here.
class machine(admin.ModelAdmin):
    list_display = ('title','time')

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js',
        )

admin.site.register(Machine,machine)