# Generated by Django 3.1.4 on 2021-01-02 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catriges', '0036_auto_20210102_1340'),
        ('workspace', '0020_auto_20210102_1340'),
        ('printers', '0045_auto_20210102_1340'),
        ('personal', '0003_delete_test'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Persons',
        ),
    ]
