# Generated by Django 3.1.4 on 2020-12-26 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catriges', '0025_auto_20201226_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartridge',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 12, 26, 16, 8, 57, 504631)),
        ),
    ]
