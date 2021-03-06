from mainapp.models import *


class MonitorModel(ProductModel):
    image = models.ImageField(verbose_name='Фото', blank=True)
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

    class Meta:
        verbose_name = 'Монитор'
        verbose_name_plural = 'Мониторы'

    def __str__(self):
        return self.serialNumber


class PCModel(ProductModel):
    image = models.ImageField(verbose_name='Фото', blank=True)

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
    # OS = models.ForeignKey(OS, models.CASCADE, verbose_name='Операционная система')
    status = models.ForeignKey(StatusWork, models.CASCADE, verbose_name='Статус')

    class Meta:
        verbose_name = 'Системный блок'
        verbose_name_plural = 'Системные блоки'

    def __str__(self):
        return self.serialNumber


class TokenModel(ProductModel):
    firm = models.ForeignKey(Firm, models.CASCADE, verbose_name='Производитель')
    image = models.ImageField(verbose_name='Фото', blank=True)

    class Meta:
        verbose_name = 'Модель Токена'
        verbose_name_plural = 'Модели токенов'

    def __str__(self):
        return self.name


class Token(Product):
    tokenModel = models.ForeignKey(TokenModel, models.CASCADE, verbose_name='Модель токена')

    class Meta:
        verbose_name = 'Токен'
        verbose_name_plural = 'Токены'

    def __str__(self):
        return self.serialNumber


class TelephoneModel(ProductModel):
    firm = models.ForeignKey(Firm, models.CASCADE, verbose_name='Производитель', null=True)
    image = models.ImageField(verbose_name='Фото', blank=True)

    class Meta:
        verbose_name = 'Модель телефона'
        verbose_name_plural = 'Модели телефонов'

    def __str__(self):
        return self.name


class Telephone(Product):
    modelTelephone = models.ForeignKey(TelephoneModel, verbose_name='Модель телефона', on_delete=models.CASCADE,
                                       blank=True)

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

    def __str__(self):
        return self.serialNumber


class PowerModel(ProductModel):
    firm = models.ForeignKey(Firm, models.CASCADE, verbose_name='Производитель', null=True)
    image = models.ImageField(verbose_name='Фото', blank=True)

    class Meta:
        verbose_name = 'Модель источника бесперебойного питания'
        verbose_name_plural = 'Модели источников бесперебойного питания'

    def __str__(self):
        return self.name


class Power(Product):
    powerModel = models.ForeignKey(TelephoneModel, verbose_name='Модель источника бесперебойного писатния',
                                   on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = 'Источник бесперебойного питания'
        verbose_name_plural = 'Истоники бесперебойного питания'

    def __str__(self):
        return self.serialNumber


class ActWorkSpace(Act):
    person = models.ForeignKey(Persons, models.CASCADE, verbose_name='Пользователь')
    monitor = models.ForeignKey(Monitor, models.CASCADE, verbose_name='Монитор')
    pc = models.ForeignKey(PC, models.CASCADE, verbose_name='Системный блок')
    token = models.ForeignKey(Token, models.CASCADE, verbose_name='Токен')
    telephone = models.ForeignKey(Telephone, verbose_name='Телефон', on_delete=models.CASCADE, blank=True, null=True)
    power = models.ForeignKey(Power, verbose_name='Источник бесперебойного питания', on_delete=models.CASCADE,
                              blank=True, null=True)

    class Meta:
        verbose_name = 'Акт'
        verbose_name_plural = 'Акты'

    def __str__(self):
        return self.number


class WorkSpaceSchedule(Schedule):
    act = models.ForeignKey(ActWorkSpace, models.CASCADE, verbose_name='Номер акта')

    class Meta:
        verbose_name = 'Журнал выдачи рабочего места'
        verbose_name_plural = 'Журналы выдачи рабочих мест'

    def __str__(self):
        return self.apper
