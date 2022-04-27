from django.db import models

# Create your models here.


class User(models.Model):
    id = models.CharField(max_length=20, verbose_name='Индификационный номер')
    FIIO = models.TextField(blank=True, verbose_name='ФИО')
    bdate = models.DateField(auto_now=True, verbose_name='Дата рождения')
    sex = models.CharField(max_length=10, verbose_name='Пол')
    email = models.EmailField(max_length=40, verbose_name='Электронная почта')
    tel = models.IntegerField(verbose_name='Телефон')
    city = models.TextField(blank=True, verbose_name='Город')
    password = models.CharField(max_length=20, verbose_name='Индификационный номер')

class reztest(models.Model):
    id = models.CharField(max_length=20, verbose_name='Индификационный номер')
    man_id = models.CharField(max_length=20, verbose_name='Индификационный номер человека')
    kompet_id = models.CharField(max_length=20, verbose_name='Индификационный номер компетенции')
    user_score = models.IntegerField(verbose_name='Баллы пользователя')
    testdate = models.DateTimeField(auto_now_add=True, name="Дата тестирования")


class etalon(models.Model):
    id = models.CharField(max_length=20, verbose_name='Индификационный номер')
    kompet_id = models.CharField(max_length=20, verbose_name='Индификационный номер компетенции')
    work_id = models.CharField(max_length=20, verbose_name='Индификационный номер компетенции')
    fullscore = models.IntegerField(verbose_name='Набрано баллов')


class kompet(models.Model):
    id = models.CharField(max_length=20, verbose_name='Индификационный номер')
    name = models.CharField(max_length=30, verbose_name='Компетенция')