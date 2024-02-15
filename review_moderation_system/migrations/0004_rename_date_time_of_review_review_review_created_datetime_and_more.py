# Generated by Django 5.0.2 on 2024-02-15 13:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_moderation_system', '0003_alter_banword_options_alter_doctor_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='date_time_of_review',
            new_name='review_created_datetime',
        ),
        migrations.AlterField(
            model_name='banword',
            name='word',
            field=models.CharField(max_length=50, unique=True, verbose_name='Матерное слово'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Врач'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialties',
            field=models.ManyToManyField(related_name='doctors', to='review_moderation_system.specialty', verbose_name='Специальности'),
        ),
        migrations.AlterField(
            model_name='exceptionword',
            name='word',
            field=models.CharField(max_length=50, unique=True, verbose_name='Слово-исключение'),
        ),
        migrations.AlterField(
            model_name='review',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='review_moderation_system.doctor'),
        ),
        migrations.AlterField(
            model_name='review',
            name='original_review',
            field=models.CharField(max_length=1000, verbose_name='Оригинальный отзыв'),
        ),
        migrations.AlterField(
            model_name='review',
            name='processed_review',
            field=models.CharField(max_length=1000, verbose_name='Обработанный отзыв'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Специальность'),
        ),
    ]