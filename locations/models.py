from django.db import models


class Titul(models.Model):
    number = models.CharField(max_length=20, verbose_name="Номер титула")
    name = models.CharField(max_length=100, verbose_name="Название титула")

    class Meta:
        verbose_name = "Титул"
        verbose_name_plural = "Титулы"
        db_table = "Titul"

    def __str__(self):
        return self.name


class Room(models.Model):
    titul = models.ForeignKey(Titul, models.CASCADE, verbose_name='Номер титула')
    number = models.CharField(max_length=100, verbose_name="Номер помещения")
    floor = models.CharField(max_length=20, verbose_name="Этаж")

    class Meta:
        verbose_name = "Помещение"
        verbose_name_plural = "Помещения"
        db_table = "Room"

    def __str__(self):
        return self.titul.name
