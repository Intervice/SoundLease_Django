# Generated by Django 5.1.7 on 2025-04-09 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_beat_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beat',
            options={'verbose_name': 'Біт', 'verbose_name_plural': 'Біти'},
        ),
        migrations.RemoveField(
            model_name='beat',
            name='pub_date',
        ),
    ]
