from django.db import models

# Create your models here.





class People(models.Model):
    id = models.CharField(max_length=20, verbose_name='Индификационный номер')
    FIIO = models.TextField(blank=True, verbose_name='ФИО')
    bdate = models.DateField(auto_now=True, verbose_name='Дата рождения')
    sex = models.CharField(max_length=10, verbose_name='Пол')
    email = models.EmailField(max_length=40, verbose_name='Электронная почта')
    tel = models.IntegerField(verbose_name='Телефон')
    city = models.TextField(blank=True, verbose_name='Город')
    hobby = models.CharField(max_length=100, verbose_name='Увлечения')
    weight = models.FloatField(verbose_name='Вес')


class work(models.Model):
    id = models.CharField(max_length=20, verbose_name='Индификационный номер')
    name = models.CharField(max_length=30, verbose_name='Профессия')