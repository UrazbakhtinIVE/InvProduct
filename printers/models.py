from locations.models import *
from mainapp.models import *


class PrinterModel(ProductModel):
    name = models.CharField(max_length=30, verbose_name="Имя в локальной сети")

    class Meta:
        verbose_name = "Модель принтера"
        verbose_name_plural = "Модели принтеров"
        db_table = "PrinterModel"

    def __str__(self):
        return self.name


class PrinterStatus(Status):
    pass

    class Meta:
        verbose_name = "Статус принтера"
        verbose_name_plural = "Статусы принтеров"
        db_table = "PrinterStatus"

    def __str__(self):
        return self.name


class Printer(Product):
    category = models.ForeignKey(Category, models.CASCADE, verbose_name="Категория")
    name = models.CharField(max_length=100, verbose_name="Имя в локальной сети", unique=True)
    ip = models.CharField(max_length=15, verbose_name="ip-адрес", blank=True)
    printerModel = models.ForeignKey(PrinterModel, models.CASCADE, verbose_name="Модель")
    firm = models.ForeignKey(Firm, models.CASCADE, verbose_name="Прозводитель")
    isColor = models.BooleanField(default=True, verbose_name="Цветной")
    printerStatus = models.ForeignKey(PrinterStatus, models.CASCADE, verbose_name="Статус")
    printerLocation = models.ForeignKey(Room, models.CASCADE, verbose_name="Месторасположение")


    class Meta:
        verbose_name = "Принтер"
        verbose_name_plural = "Принтеры"
        db_table = "Printer"

    def __str__(self):
        return self.serialNumber


"""Журнал должен  хранить историю состояния и месторасположение принтера """


# Журнал принтеров
class PrinterSchedule(Schedule):
    printer = models.ForeignKey(Printer, models.CASCADE, verbose_name="Принтер")
    status = models.ForeignKey(PrinterStatus, models.CASCADE, verbose_name="Статус")
    room = models.ForeignKey(Room, models.CASCADE, verbose_name="Место расположение")

    class Meta:
        verbose_name = "Журнал принтера"
        verbose_name_plural = "Журналы принтеров"

    def __str__(self):
        return self.printer.name


# Заявка на обслуживания принтера
class PrinterApplication(Applications):
    printer = models.ManyToManyField(Printer, verbose_name="Серийный номер")

    class Meta:
        verbose_name = "Заявка на обслуживание принтера"
        verbose_name_plural = "Заявки на обслуживание принтеров"

    def __str__(self):
        return self.printer.serialNumber


# Акт передачи принтеров
class PrinterAct(Act):
    serialNumber = models.ManyToManyField(Printer, verbose_name="Серийный номер")

    class Meta:
        verbose_name = "Акт передачи принтера"
        verbose_name_plural = "Акты передачи принтеров"

    def __str__(self):
        return self.number
