from django.db import models
from django.contrib.auth.models import User

# Save until checking


class Specialty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    specialties = models.ManyToManyField(Specialty)

    def __str__(self):
        return self.name


class Review(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    original_review = models.TextField()
    processed_review = models.TextField()
    ip_address = models.GenericIPAddressField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Review for {self.doctor.name} from {self.user} on {self.date}"


class BanWord(models.Model):
    word = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.word


class ExceptionWord(models.Model):
    word = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.word
