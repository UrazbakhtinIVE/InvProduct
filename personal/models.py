from django.db import models

from locations.models import Room


class Post(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название должности")
    telephone = models.CharField(max_length=12, verbose_name='Телефон', blank=True)
    email = models.EmailField(blank=True)
    isChangePost = models.BooleanField(verbose_name='Сменый персонал')
    isVip = models.BooleanField(default=False, verbose_name='Высшее руководство')
    room = models.ForeignKey(Room, models.CASCADE, verbose_name="Место расположение", null=True )

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name



class Department(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название отдела")



    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.name


class Persons(models.Model):
    firstName = models.CharField(max_length=50, verbose_name='Фамилия')
    lastName = models.CharField(max_length=50, verbose_name='Имя')
    fatherName = models.CharField(max_length=50, verbose_name='Отчество')
    department = models.ManyToManyField(Department, verbose_name='Отдел')
    posts = models.ManyToManyField(Post, verbose_name='Должность')
    email = models.EmailField(verbose_name="Эл.почта", blank=True)
    photo = models.ImageField(verbose_name="Фото", blank=True)
    workTelephone = models.CharField(max_length=15, verbose_name='Внутрений номер', blank=True)
    mobileTelephone = models.CharField(max_length=15, verbose_name='Мобильный телефон', blank=True)


    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.firstName





