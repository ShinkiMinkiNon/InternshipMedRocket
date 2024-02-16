from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .forms import ReviewForm
from .models import Doctor


def add_review(request: HttpRequest, doctor_id) -> HttpResponse:
    #   Накинуть валидаторов, что происходит когда отправляют форму, убрать возможность повторной отправки
    #   Понять где тут подтягиваются специальности и выбрать между select_ и prefetch_ related
    #

    doctor = Doctor.objects.get(id=doctor_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_text = request.POST['review_text']
            if len(review_text) < 100:
                return HttpResponse('Должно быть хотя бы 100 символов')
            else:
                return HttpResponse('Отзыв успешно отправлен')
    else:
        initial_data = {
            'doctor_name': doctor.full_name,
        }
        form = ReviewForm(initial=initial_data)
    return render(request, 'add-review.html', context={'form': form, 'doctor': doctor})
