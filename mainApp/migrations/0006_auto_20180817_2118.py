# Generated by Django 2.0.5 on 2018-08-17 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_auto_20180811_2310'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Events',
        ),
        migrations.DeleteModel(
            name='SubscribeModel',
        ),
    ]
