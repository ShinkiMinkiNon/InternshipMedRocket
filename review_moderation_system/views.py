from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.utils import timezone

from .forms import ReviewForm
from .models import Doctor, Review


def add_review(request: HttpRequest, doctor_id):
    doctor = get_object_or_404(Doctor.objects.prefetch_related('specialties'), id=doctor_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_text = form.cleaned_data['original_review']
            if len(review_text) < 100:
                return HttpResponse('Должно быть хотя бы 100 символов', status=400)
            else:
                ip_address = request.META.get('REMOTE_ADDR')
                user = request.user
                review = Review.objects.create(
                    original_review=review_text,
                    ip_address=ip_address,
                    doctor_id=doctor.pk,
                    user_id=user.id,
                    review_created_datetime=timezone.now()
                )
                review.save()
                return redirect('review_success_page')
    else:
        initial_data = {'doctor_name': doctor.full_name}
        form = ReviewForm(initial=initial_data)
    return render(request, 'add-review.html', {'form': form, 'doctor': doctor})


def review_success_page(request: HttpRequest):
    return HttpResponse('Отзыв успешно отправлен')
