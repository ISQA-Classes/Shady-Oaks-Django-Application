# Generated by Django 2.0.5 on 2018-11-29 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_teetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teetime',
            name='Equipment_Rentals',
        ),
    ]