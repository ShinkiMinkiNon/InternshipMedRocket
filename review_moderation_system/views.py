from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest


from .forms import ReviewForm
from .models import Doctor, Review


def add_review(request, doctor_id):
    doctor = Doctor.objects.prefetch_related('specialties').get(id=doctor_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_text = form.cleaned_data['review_text']
            if len(review_text) < 100:
                # Если длина отзыва меньше 100 символов, возвращаем сообщение об ошибке
                return HttpResponse('Должно быть хотя бы 100 символов', status=400)
            else:
                # Сохраняем отзыв и перенаправляем пользователя
                review = Review.objects.create()
                review.owner = form.cleaned_data['review_text']
                review.doctor = doctor
                review.ip_address = request.META.get('REMOTE_ADDR')
                if request.user.is_authenticated:
                    review.user = request.user
                review.save()
                # После успешного сохранения перенаправляем пользователя
                return redirect('success_page_url')
    else:
        initial_data = {'doctor_name': doctor.full_name}
        form = ReviewForm(initial=initial_data)
    return render(request, 'add-review.html', {'form': form, 'doctor': doctor})
