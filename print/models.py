from django.urls import reverse

from locations.models import Room
from mainapp.models import *


class PrinterStatus(Status):
    pass

    class Meta:
        verbose_name = "Статус принтера"
        verbose_name_plural = "Статусы принтеров"

    def __str__(self):
        return self.name


class CartridgeStatus(Status):
    pass

    class Meta:
        verbose_name = "Статус картриджа"
        verbose_name_plural = "Статусы картриджей"

    def __str__(self):
        return self.name


class PrinterModel(ProductModel):
    CHOICES = (
        ('l', 'Лазерный'),
        ('s', 'Струйныйй'),
    )
    type = models.CharField(max_length=20, choices=CHOICES, verbose_name='Тип принтера')
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, verbose_name="Производитель")
    image = models.ImageField(verbose_name='Изображение')

    class Meta:
        verbose_name = 'Модель принтера'
        verbose_name_plural = 'Модель принтеров'

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    word = models.CharField(max_length=1, verbose_name='Обозначение')

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class CartridgeModel(ProductModel):
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, verbose_name="Производитель")
    image = models.ImageField(verbose_name='Изображение')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name="Производитель")

    class Meta:
        verbose_name = 'Модель картриджа'
        verbose_name_plural = 'Модель картриджа'

    def __str__(self):
        return self.name


class Cartridge(Product):
    cartridgeModel = models.ForeignKey(CartridgeModel, on_delete=models.CASCADE, verbose_name='Модель принтера')
    status = models.ForeignKey(CartridgeStatus, models.CASCADE, verbose_name="Статус картриджа")

    class Meta:
        verbose_name = 'Картридж'
        verbose_name_plural = 'Картриджи'

    def __str__(self):
        return self.serialNumber


class Printer(Product):
    printerModel = models.ForeignKey(PrinterModel, on_delete=models.CASCADE, verbose_name='Модель принтера')
    name = models.CharField(max_length=100, verbose_name="имя принтера в сети")
    ip = models.CharField(max_length=15, verbose_name="ip-адрес")
    status = models.ForeignKey(PrinterStatus, models.CASCADE, verbose_name="Статус принтера")
    cartridge = models.ManyToManyField(Cartridge, verbose_name='Установленые картриджи')

    class Meta:
        verbose_name = 'Принтер'
        verbose_name_plural = 'Принтеры'

    def __str__(self):
        return self.serialNumber


class PrinterSchedule(Schedule):
    printer = models.ForeignKey(Printer, models.CASCADE, verbose_name="Принтер")
    status = models.ForeignKey(PrinterStatus, models.CASCADE, verbose_name="Статус")
    location = models.ForeignKey(Room, models.CASCADE, verbose_name="Место расположение")

    class Meta:
        verbose_name = "Журнал принтера"
        verbose_name_plural = "Журналы принтеров"

    def get_absolute_url(self):
        return reverse('printerScheduleList')

    def __str__(self):
        return self.printer.name


class PrinterAct(Act):
    printer = models.ManyToManyField(Printer, verbose_name='Серийный номер')

    def __str__(self):
        return self.printer.serialNumber

    class Meta:
        verbose_name = "Акт передачи принтера"
        verbose_name_plural = "Акты передачи принтеров"



class CatrigeAct(Act):
    catrige = models.ManyToManyField(Cartridge, verbose_name="Картридж")

    def __str__(self):
        return self.catrige.serialNumber

    class Meta:
        verbose_name = "Акт передачи картриджа"
        verbose_name_plural = "Акты передачи картриджей"

