# Generated by Django 3.1.4 on 2021-01-08 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('print', '0010_auto_20210108_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printermodel',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Изображение'),
        ),
    ]
