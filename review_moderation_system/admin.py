from django.contrib import admin
from django import forms
from .models import *


@admin.register(Review)
class Review(admin.ModelAdmin):
    list_display = ['doctor', 'review_created_datetime', 'original_review', 'processed_review', 'ip_address', 'user']
    search_fields = ['doctor__name', 'original_review', 'user__username']
    readonly_fields = ['review_created_datetime']
    raw_id_fields = ['doctor']

    def has_change_permission(self, request, obj=None):
        return True

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return [field.name for field in obj._meta.fields if field.name != 'processed_review']
        return ['processed_review', 'review_created_datetime']

    ordering = []

    fieldsets = [
        (None, {'fields': ['doctor', 'review_created_datetime', 'user']}),
        ('Review', {'fields': ['original_review', 'processed_review'], 'classes': ['vLargeTextField', 'wide']}),
        ('IP Address', {'fields': ['ip_address'], 'classes': ['collapse']}),
    ]

    formfield_overrides = {
        models.CharField: {'widget': forms.Textarea}
    }


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
    search_fields = ['full_name']
    list_display = ['full_name']
