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
    list_display = ['doctor', 'date_time_of_review', 'original_review', 'processed_review', 'ip_address', 'user']
    search_fields = ['doctor__name', 'original_review', 'user__username']
    readonly_fields = ['date_time_of_review', 'original_review']

    ordering = []

    def has_change_permission(self, request, obj=None):
        return False

    fieldsets = [
        (None, {'fields': ['doctor', 'date_time_of_review', 'user']}),
        ('Review', {'fields': ['processed_review', 'original_review'], 'classes': ['wide']}),
        ('IP Address', {'fields': ['ip_address'], 'classes': ['collapse']}),
    ]
