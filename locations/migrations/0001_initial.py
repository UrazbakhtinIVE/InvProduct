# Generated by Django 3.1.4 on 2020-12-18 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Titul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, verbose_name='Номер титула')),
                ('name', models.CharField(max_length=100, verbose_name='Название титула')),
            ],
            options={
                'verbose_name': 'Титул',
                'verbose_name_plural': 'Титулы',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100, verbose_name='Номер помещения')),
                ('floor', models.CharField(max_length=20, verbose_name='Этаж')),
                ('titul', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.titul', verbose_name='Номер титула')),
            ],
            options={
                'verbose_name': 'Помещение',
                'verbose_name_plural': 'Помещения',
            },
        ),
    ]
