# Generated by Django 5.1.7 on 2025-04-30 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_beat_cover_image_alter_beat_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beat',
            name='slug',
            field=models.SlugField(verbose_name='Слаг'),
        ),
    ]
