# Generated by Django 5.1.7 on 2025-04-09 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beat',
            name='slug',
            field=models.SlugField(verbose_name='Слаг'),
        ),
    ]
