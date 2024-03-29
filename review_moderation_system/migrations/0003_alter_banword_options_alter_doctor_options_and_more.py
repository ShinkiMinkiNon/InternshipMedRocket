# Generated by Django 5.0.2 on 2024-02-14 13:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_moderation_system', '0002_rename_exception_exceptionword'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banword',
            options={'verbose_name': 'Запрещенное слово', 'verbose_name_plural': 'Запрещенные слова'},
        ),
        migrations.AlterModelOptions(
            name='doctor',
            options={'verbose_name': 'Врач', 'verbose_name_plural': 'Врачи'},
        ),
        migrations.AlterModelOptions(
            name='exceptionword',
            options={'verbose_name': 'Слово-исключение', 'verbose_name_plural': 'Слова-исключения'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterModelOptions(
            name='specialty',
            options={'verbose_name': 'Специальность', 'verbose_name_plural': 'Специальности'},
        ),
        migrations.RenameField(
            model_name='review',
            old_name='date',
            new_name='date_time_of_review',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialties',
            field=models.ManyToManyField(related_name='doctors', to='review_moderation_system.specialty'),
        ),
        migrations.AlterField(
            model_name='review',
            name='original_review',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='review',
            name='processed_review',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
