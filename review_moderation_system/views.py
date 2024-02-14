from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Doctor, Review


def add_review(request: HttpRequest, doctor_id) -> HttpResponse:
    doctor = Doctor.objects.get(id=doctor_id)
    context = {
        'doctor': doctor
    }
    if request.method == 'POST':
        review_text = request.POST['review_text']
        if len(review_text) < 100:
            return HttpResponse('Должно быть хотя бы 100 символов')
        else:
            review = Review().objects.create(doctor=doctor, original_text=review_text)
            return HttpResponse('Отзыв успешно отправлн')
    return render(request, 'add-review.html', context=context)
