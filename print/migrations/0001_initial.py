# Generated by Django 3.1.4 on 2021-01-07 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0002_auto_20201219_0024'),
        ('mainapp', '0006_delete_acts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True, verbose_name='Дата передачи')),
                ('serialNumber', models.CharField(max_length=100, unique=True, verbose_name='Серийный номер')),
            ],
            options={
                'verbose_name': 'Картридж',
                'verbose_name_plural': 'Картриджи',
            },
        ),
        migrations.CreateModel(
            name='CartridgeStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус картриджа',
                'verbose_name_plural': 'Статусы картриджей',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('word', models.CharField(max_length=1, verbose_name='Обозначение')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True, verbose_name='Дата передачи')),
                ('serialNumber', models.CharField(max_length=100, unique=True, verbose_name='Серийный номер')),
                ('name', models.CharField(max_length=100, verbose_name='имя принтера в сети')),
                ('ip', models.CharField(max_length=15, verbose_name='ip-адрес')),
                ('cartridge', models.ManyToManyField(to='print.Cartridge', verbose_name='Установленые картриджи')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.room', verbose_name='Место расположение')),
            ],
            options={
                'verbose_name': 'Принтер',
                'verbose_name_plural': 'Принтеры',
            },
        ),
        migrations.CreateModel(
            name='PrinterStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус принтера',
                'verbose_name_plural': 'Статусы принтеров',
            },
        ),
        migrations.CreateModel(
            name='PrinterSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apper', models.CharField(max_length=100, unique=True, verbose_name='Номер заявки')),
                ('date', models.DateField(verbose_name='Дата')),
                ('description', models.TextField(blank=True, verbose_name='Примечание')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.room', verbose_name='Место расположение')),
                ('printer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='print.printer', verbose_name='Принтер')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='print.printerstatus', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Журнал принтера',
                'verbose_name_plural': 'Журналы принтеров',
            },
        ),
        migrations.CreateModel(
            name='PrinterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название модели')),
                ('type', models.CharField(choices=[('l', 'Лазерный'), ('s', 'Струйныйй')], max_length=20, verbose_name='Тип принтера')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('firm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.firm', verbose_name='Производитель')),
            ],
            options={
                'verbose_name': 'Модель принтера',
                'verbose_name_plural': 'Модель принтеров',
            },
        ),
        migrations.AddField(
            model_name='printer',
            name='printerModel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='print.printermodel', verbose_name='Модель принтера'),
        ),
        migrations.AddField(
            model_name='printer',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='print.printerstatus', verbose_name='Статус принтера'),
        ),
        migrations.CreateModel(
            name='CartridgeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название модели')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='print.color', verbose_name='Производитель')),
                ('firm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.firm', verbose_name='Производитель')),
            ],
            options={
                'verbose_name': 'Модель картриджа',
                'verbose_name_plural': 'Модель картриджа',
            },
        ),
        migrations.AddField(
            model_name='cartridge',
            name='cartridgeModel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='print.cartridgemodel', verbose_name='Модель принтера'),
        ),
        migrations.AddField(
            model_name='cartridge',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='cartridge',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.room', verbose_name='Месторасположение'),
        ),
        migrations.AddField(
            model_name='cartridge',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='print.cartridgestatus', verbose_name='Статус картриджа'),
        ),
    ]
