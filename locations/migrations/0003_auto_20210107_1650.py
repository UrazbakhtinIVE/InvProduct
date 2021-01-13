# Generated by Django 3.1.4 on 2021-01-07 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20201219_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default=1, max_length=100, verbose_name='Название помещения'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='titulName',
            field=models.CharField(default=2, max_length=100, unique=True, verbose_name='Название титула'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='titul',
            field=models.CharField(max_length=10, unique=True, verbose_name='Номер титула'),
        ),
        migrations.DeleteModel(
            name='Titul',
        ),
    ]