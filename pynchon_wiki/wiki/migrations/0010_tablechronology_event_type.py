# Generated by Django 3.2.16 on 2023-09-29 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0009_auto_20230909_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablechronology',
            name='event_type',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Тип события'),
        ),
    ]
