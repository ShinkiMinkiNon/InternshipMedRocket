from django.contrib import admin
from .models import *
from django import forms


# class ReviewAdminForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.initial_review = self.instance.review.original_review
#
#     def clean_original_review(self):
#         initial_review = self.initial_review
#         new_review = self.cleaned_data['original_review']
#         if initial_review != new_review:
#             self.fields['original_review'].widget.attrs['readonly'] = True
#             self.fields['processed_review'].widget.attrs['readonly'] = False
#         return new_review


@admin.register(Review)
class Review(admin.ModelAdmin):
    list_display = ['doctor', 'review_created_datetime', 'original_review', 'processed_review', 'ip_address', 'user']
    search_fields = ['doctor__name', 'original_review', 'user__username']
    readonly_fields = ['review_created_datetime']

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
