from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .forms import ReviewForm
from .models import Doctor, Review


def add_review(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_text = request.POST['review_text']
            if len(review_text) < 100:
                return HttpResponse('Должно быть хотя бы 100 символов')
            else:
                return HttpResponse('Отзыв успешно отправлен')
    else:
        form = ReviewForm()
    return render(request, 'add-review.html', context={'form': form})
