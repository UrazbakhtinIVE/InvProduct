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
        verbose_name = 'Статус Монитора'
        verbose_name_plural = 'Статусы Мониторов'

    def __str__(self):
        return self.name


class Monitor(models.Model):
    category = models.ForeignKey(Category, models.CASCADE, verbose_name='Категория')
    model = models.ForeignKey(MonitorModel, models.CASCADE, verbose_name='Модель')
    serialNumber = models.CharField(max_length=100, verbose_name='Серийный номер')
    status = models.ForeignKey(StatusWork, models.CASCADE, verbose_name='Статус')
    loc = models.BooleanField(max_length=100, verbose_name='У сотрудника на УД')

    class Meta:
        verbose_name = 'Монитор'
        verbose_name_plural = 'Мониторы'
