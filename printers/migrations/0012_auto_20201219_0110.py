# Generated by Django 3.1.4 on 2020-12-18 22:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printers', '0011_auto_20201219_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printer',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 12, 19, 1, 10, 20, 398782)),
        ),
    ]
