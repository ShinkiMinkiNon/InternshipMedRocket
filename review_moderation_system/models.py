from django.db import models
from django.contrib.auth.models import User

# Save until checking


class Specialty(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    specialties = models.ManyToManyField(Specialty, related_name='doctors')

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'

    def __str__(self):
        return self.name


class Review(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date_time_of_review = models.DateTimeField(auto_now_add=True)
    original_review = models.CharField(max_length=1000)
    processed_review = models.CharField(max_length=1000)
    ip_address = models.GenericIPAddressField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return (f"Отзыв для: {self.doctor.name}\n"
                f"От: {self.user}\n"
                f"Когда: {self.date_time_of_review}")


class BanWord(models.Model):
    word = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Запрещенное слово'
        verbose_name_plural = 'Запрещенные слова'

    def __str__(self):
        return self.word


class ExceptionWord(models.Model):
    word = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Слово-исключение'
        verbose_name_plural = 'Слова-исключения'

    def __str__(self):
        return self.word
