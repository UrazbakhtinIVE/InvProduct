# Generated by Django 3.1.4 on 2020-12-18 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='room',
            table='Room',
        ),
        migrations.AlterModelTable(
            name='titul',
            table='Titul',
        ),
    ]