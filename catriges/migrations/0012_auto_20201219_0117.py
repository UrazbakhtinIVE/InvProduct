# Generated by Django 3.1.4 on 2020-12-18 22:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catriges', '0011_auto_20201219_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartridge',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 12, 19, 1, 17, 44, 817083)),
        ),
    ]
