from django.contrib import admin
from .models import userinfo
# Register your models here.
class user(admin.ModelAdmin):
    list_display = ('username', 'password')


admin.site.register(userinfo,user)