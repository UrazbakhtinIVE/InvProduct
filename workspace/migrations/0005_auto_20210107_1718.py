# Generated by Django 3.1.4 on 2021-01-07 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0005_auto_20210107_1709'),
        ('workspace', '0004_auto_20210107_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.room', verbose_name='Место расположение'),
        ),
        migrations.AddField(
            model_name='pc',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.room', verbose_name='Место расположение'),
        ),
        migrations.AddField(
            model_name='power',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.room', verbose_name='Место расположение'),
        ),
        migrations.AddField(
            model_name='telephone',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.room', verbose_name='Место расположение'),
        ),
        migrations.AddField(
            model_name='token',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.room', verbose_name='Место расположение'),
        ),
    ]