# Generated by Django 3.1.4 on 2020-12-21 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('mainapp', '0004_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Telephone',
        ),
    ]
