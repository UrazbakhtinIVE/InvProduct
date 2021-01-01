from django.urls import reverse
from printers.models import *


class Color(models.Model):
    name = models.CharField(max_length=100, verbose_name="Цвет", unique=True)
    word = models.CharField(max_length=1, verbose_name="Обозначение")

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"

    def __str__(self):
        return self.name


class CartridgeModel(ProductModel):
    color = models.ForeignKey(Color, models.CASCADE, verbose_name="Цвет")
    img = models.ImageField(blank=True, verbose_name="Фото")

    class Meta:
        verbose_name = "Модель картриджа"
        verbose_name_plural = "Модели картриджей"

    def __str__(self):
        return self.name


class CatrigeStatus(Status):
    pass

    class Meta:
        verbose_name = "Статус картриджа"
        verbose_name_plural = "Статусы картриджей"
        db_table = "CatrigeStatus"

    def __str__(self):
        return self.name


class Cartridge(Product):
    CartridgeModel = models.ForeignKey(CartridgeModel, models.CASCADE, verbose_name="Модель картриджа")
    original = models.BooleanField(verbose_name="Оригинальный")
    status = models.ForeignKey(CatrigeStatus, on_delete=models.CASCADE, verbose_name="Статус картриджа")
    printer = models.ForeignKey(Printer, null=True, on_delete=models.SET_NULL, verbose_name="Установлен в принтере",
                                related_name='cartridges')

    class Meta:
        verbose_name = "Картридж"
        verbose_name_plural = " Картриджи"
        db_table = "Cartridge"

    def get_absolute_url(self):
        return reverse('cartridgeList')

    def __str__(self):
        return self.serialNumber


class CartridgeApplication(Applications):
    cartridge = models.ManyToManyField(Cartridge, verbose_name="Серийный номер")

    class Meta:
        verbose_name = "Заявка на обслуживание картриджа"
        verbose_name_plural = "Заявки на обслуживание картриджей"

    def __str__(self):
        return self.cartridge.serialNumber


# Акт передачи принтеров
class CartridgeAct(Act):
    serialNumber = models.ManyToManyField(Printer, verbose_name="Серийный номер")

    class Meta:
        verbose_name = "Акт передачи принтера"
        verbose_name_plural = "Акты передачи принтеров"

    def __str__(self):
        return self.number


# Журнал картриджей
class PrinterSchedule(Schedule):
    catrige = models.ForeignKey(Cartridge, models.CASCADE, verbose_name="Картридж")
    status = models.ForeignKey(CatrigeStatus, models.CASCADE, verbose_name="Статус")


    class Meta:
        verbose_name = "Журнал картриджа"
        verbose_name_plural = "Журналы картриджей"

    def __str__(self):
        return self.apper