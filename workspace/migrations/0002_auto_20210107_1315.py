# Generated by Django 3.1.4 on 2021-01-07 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monitor',
            name='date',
        ),
        migrations.RemoveField(
            model_name='pc',
            name='date',
        ),
        migrations.RemoveField(
            model_name='power',
            name='date',
        ),
        migrations.RemoveField(
            model_name='telephone',
            name='date',
        ),
        migrations.RemoveField(
            model_name='token',
            name='date',
        ),
    ]
