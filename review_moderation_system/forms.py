from django import forms


class ReviewForm(forms.Form):
    doctor_name = forms.CharField(label='ФИО врача')
    specialties = forms.CharField(label='Специальности')
    review_text = forms.CharField(label='Ваш отзыв', widget=forms.Textarea)