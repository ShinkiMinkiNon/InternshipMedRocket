from django.contrib import admin
from .models import *


class BanWordAdmin(admin.ModelAdmin):
    list_display = 'pk', 'word'
    list_display_links = 'pk', 'word'


admin.site.register(BanWord, BanWordAdmin)

# Register your models here.
