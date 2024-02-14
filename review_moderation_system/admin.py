from django.contrib import admin
from django import forms
from .models import *


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(BanWord)
class BanWordAdmin(admin.ModelAdmin):
    search_fields = ['word']


@admin.register(ExceptionWord)
class ExceptionAdmin(admin.ModelAdmin):
    search_fields = ['word']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']


@admin.register(Review)
class Review(admin.ModelAdmin):
    list_display = ['doctor', 'date', 'original_review', 'processed_review', 'ip_address', 'user']
    search_fields = ['doctor__name', 'original_review', 'ip_address', 'user__username']
    readonly_fields = ['date', 'original_review']

    def has_change_permission(self, request, obj=None):
        return False

    # fieldsets = [
    #     (None, {'fields': ['doctor__name', 'ip_address', 'user', '']}),
    #     ('Review', {'fields': ['processed_review'], 'classes': ['wide']})
    # ]
    #
    # formfield_overrides = {
    #     models.TextField: {'widget': forms.Textarea(attrs={'rows': 5, 'cols': 10})}
    # }
