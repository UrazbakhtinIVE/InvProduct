# Generated by Django 3.1.4 on 2020-12-18 21:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catriges', '0002_catrige_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catrige',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 12, 19, 0, 24, 28, 445752)),
        ),
    ]
