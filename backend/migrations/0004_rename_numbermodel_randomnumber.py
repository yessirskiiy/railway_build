# Generated by Django 3.2.18 on 2024-03-26 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_numbermodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NumberModel',
            new_name='RandomNumber',
        ),
    ]
