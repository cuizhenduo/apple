from django.contrib import admin
from .models import zhuanjia
# Register your models here.
class prof(admin.ModelAdmin):
    list_display = ('profname', 'password')


admin.site.register(zhuanjia,prof)