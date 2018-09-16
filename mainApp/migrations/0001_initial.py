# Generated by Django 2.0.5 on 2018-08-06 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desciption', models.TextField(max_length=400)),
                ('link', models.URLField(unique=True)),
                ('pic', models.ImageField(blank=True, upload_to='uploads')),
            ],
        ),
    ]
