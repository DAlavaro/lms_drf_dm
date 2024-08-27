# app/lms/models
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название курса')
    image = models.ImageField(upload_to='courses/', blank=True, null=True, verbose_name='Изображение курса')
    description = models.TextField(verbose_name='Описание курса', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока', null=True, blank=True)
    image = models.ImageField(upload_to='lessons/', blank=True, null=True, verbose_name='Изображение урока')
    video = models.FileField(upload_to='lessons/', blank=True, null=True, verbose_name='Видео урока')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'