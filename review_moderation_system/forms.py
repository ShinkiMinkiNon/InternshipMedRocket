from django import forms
# from .models import Review


class ReviewForm(forms.Form):
    # doctor_name = forms.CharField(label='ФИО врача')
    # specialties = forms.CharField(label='Специальности')
    review_text = forms.CharField(label='Ваш отзыв', widget=forms.Textarea)

# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ['doctor']
#     review = forms.CharField(max_length=1000, widget=forms.Textarea)
