# Generated by Django 2.2.19 on 2022-10-09 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0012_auto_20221009_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка'),
        ),
    ]