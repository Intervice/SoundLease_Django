# Generated by Django 5.1.7 on 2025-04-19 13:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_beat_premium_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='beat',
            name='premium_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Преміум ціна'),
        ),
    ]
