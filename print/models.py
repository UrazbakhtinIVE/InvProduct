from django.urls import reverse
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


class Type(models.Model):
    name = models.CharField(max_length=30, verbose_name="Наименование")

    class Meta:
        verbose_name = "Тип принтера"
        verbose_name_plural = "Типы принтеров"

    def __str__(self):
        return self.name


class PrinterModel(ProductModel):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='Тип принтера', null=True)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, verbose_name="Производитель")
    image = models.ImageField(verbose_name='Изображение', blank=True)

    class Meta:
        verbose_name = 'Модель принтера'
        verbose_name_plural = 'Модель принтеров'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('printer_model_list')


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
    location = models.ForeignKey(Room, models.CASCADE, verbose_name="Место расположение", null=True)
    cartridge = models.ManyToManyField(Cartridge, verbose_name='Установленые картриджи', blank=True)

    class Meta:
        verbose_name = 'Принтер'
        verbose_name_plural = 'Принтеры'

    def get_absolute_url(self):
        return reverse('printer_list')

    def __str__(self):
        return self.serialNumber


class PrinterSchedule(Schedule):
    printer = models.ForeignKey(Printer, models.CASCADE, verbose_name="Принтер")
    status = models.ForeignKey(PrinterStatus, models.CASCADE, verbose_name="Статус")
    location = models.ForeignKey(Room, models.CASCADE, verbose_name="Место расположение")

    class Meta:
        verbose_name = "Журнал принтера"
        verbose_name_plural = "Журналы принтеров"

    @staticmethod
    def get_absolute_url():
        return reverse('printerScheduleList')

    def __str__(self):
        return self.apper


class PrinterApp(Applications):
    printerShedule = models.ForeignKey(PrinterSchedule, models.CASCADE, verbose_name='Заявка из журнала')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.printerShedule.apper





class PrinterAct(Act):
    printer = models.ManyToManyField(Printer, verbose_name='Серийный номер')

    def __str__(self):
        return self.printer.name

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
