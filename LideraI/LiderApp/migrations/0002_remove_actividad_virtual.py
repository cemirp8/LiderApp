# Generated by Django 4.0.4 on 2022-06-04 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LiderApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actividad',
            name='virtual',
        ),
    ]
