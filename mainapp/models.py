from personal.models import *


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Firm(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    img = models.ImageField(verbose_name='Логотип', blank=True)

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    name = models.CharField(max_length=40, verbose_name="Название модели")

    class Meta:
        abstract = True


class Status(models.Model):
    name = models.CharField(max_length=20, verbose_name="Статус")

    class Meta:
        abstract = True


class Product(models.Model):
    category = models.ForeignKey(Category, models.CASCADE, verbose_name="Категория")
    serialNumber = models.CharField(max_length=100, verbose_name="Серийный номер", unique=True)

    class Meta:
        abstract = True


"""Общий класс для заявок"""


class Applications(models.Model):
    number = models.CharField(max_length=100, verbose_name="Номер заявки", unique=True)
    descriptions = models.TextField(verbose_name="Описание")
    date = models.DateField(auto_now_add=True )
    status = models.BooleanField(verbose_name="Выполнена")

    class Meta:
        abstract = True


class Schedule(models.Model):
    apper = models.CharField(max_length=100, verbose_name="Номер заявки", unique=True)
    date = models.DateField(verbose_name="Дата")
    description = models.TextField(verbose_name="Примечание", blank=True)

    class Meta:
        abstract = True


"""Общий класс для акта передачи техники"""


class Act(models.Model):
    CHOICES = (
        ('extradition', 'Выдача'),
        ('pass', 'Сдача'),
    )
    type = models.CharField(max_length=20, choices=CHOICES, verbose_name='Тип акта', null=True)
    number = models.CharField(max_length=100, verbose_name="Номер акта", unique=True)
    person = models.ForeignKey(Persons, models.CASCADE, verbose_name="Пользователь", null=True )
    file = models.FileField(verbose_name='Акт передачи', blank=True)
    date = models.DateField(verbose_name='Дата передачи')


    class Meta:
        abstract = True

