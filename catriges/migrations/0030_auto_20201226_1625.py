# Generated by Django 3.1.4 on 2020-12-26 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catriges', '0029_auto_20201226_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartridge',
            name='date_create',
            field=models.DateField(auto_now=True),
        ),
    ]
