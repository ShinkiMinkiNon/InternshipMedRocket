from django.db import models
from django.contrib.auth.models import User


class Specialty(models.Model):
    name = models.CharField(max_length=100, verbose_name="Специальность", unique=True)

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'

    def __str__(self):
        return self.name


class Doctor(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=100, verbose_name="Отчество")
    specialties = models.ManyToManyField(Specialty, related_name='doctors', verbose_name="Специальности")

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    def __str__(self):
        return self.full_name


class Review(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='reviews')
    review_created_datetime = models.DateTimeField(auto_now_add=True)
    original_review = models.CharField(max_length=1000, verbose_name="Оригинальный отзыв")
    processed_review = models.CharField(max_length=1000, verbose_name="Обработанный отзыв", null=True, blank=True)
    ip_address = models.GenericIPAddressField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return (f"Отзыв для: {self.doctor.full_name}. "
                f"От: {self.user}. "
                f"Когда: {self.review_created_datetime}.")


class BanWord(models.Model):
    word = models.CharField(max_length=50, unique=True, verbose_name="Матерное слово")

    class Meta:
        verbose_name = 'Запрещенное слово'
        verbose_name_plural = 'Запрещенные слова'

    def __str__(self):
        return self.word


class ExceptionWord(models.Model):
    word = models.CharField(max_length=50, unique=True, verbose_name="Слово-исключение")

    class Meta:
        verbose_name = 'Слово-исключение'
        verbose_name_plural = 'Слова-исключения'

    def __str__(self):
        return self.word
