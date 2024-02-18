from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['original_review']
    original_review = forms.CharField(max_length=1000, widget=forms.Textarea, label='Ваш отзыв: ')
