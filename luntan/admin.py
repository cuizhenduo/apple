from django.contrib import admin
from .models import luntan
# Register your models here.
class Luntan(admin.ModelAdmin):
    list_display = ('title', 'time')

