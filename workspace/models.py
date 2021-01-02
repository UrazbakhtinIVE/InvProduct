from mainapp.models import *


class MonitorModel(ProductModel):
    diagonal = models.IntegerField('Диагональ', blank=True)
    firm = models.ForeignKey(Firm, models.CASCADE, verbose_name='Производитель')

    class Meta:
        verbose_name = 'Модель мониторов'
        verbose_name_plural = 'Модели мониторов'

    def __str__(self):
        return self.name


class StatusWork(Status):
    pass

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name


class Monitor(Product):
    category = models.ForeignKey(Category, models.CASCADE, verbose_name='Категория')
    model = models.ForeignKey(MonitorModel, models.CASCADE, verbose_name='Модель')
    serialNumber = models.CharField(max_length=100, verbose_name='Серийный номер')
    status = models.ForeignKey(StatusWork, models.CASCADE, verbose_name='Статус')
    loc = models.BooleanField(max_length=100, verbose_name='У сотрудника на УД')

    class Meta:
        verbose_name = 'Монитор'
        verbose_name_plural = 'Мониторы'


class PCModel(ProductModel):
    class Meta:
        verbose_name = 'Модель системного блока'
        verbose_name_plural = 'Модели системных блоков'

    def __str__(self):
        return self.name




class OS(models.Model):
    name = models.CharField(max_length=30, verbose_name="Операционная система")

    class Meta:
        verbose_name = 'Операционная система'
        verbose_name_plural = 'Операционные системы'

    def __str__(self):
        return self.name



class PC(Product):
    name = models.CharField(max_length=100, verbose_name="Имя компьютера")
    HDD = models.IntegerField(verbose_name='Жесктий диск', null=True, blank=True)
    RAM = models.IntegerField(verbose_name='Оперативная память', null=True, blank=True)
    OS = models.ForeignKey(OS,models.CASCADE, verbose_name='Операционная система')
    status = models.ForeignKey(StatusWork, models.CASCADE, verbose_name='Статус')
    loc = models.BooleanField(max_length=100, verbose_name='У сотрудника на УД')

    class Meta:
        verbose_name = 'Системный блок'
        verbose_name_plural = 'Системные блоки'

    def __str__(self):
        return self.serialNumber
