# Generated by Django 3.2.16 on 2023-08-29 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0007_alter_tableсharacters_value_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='chapter',
        ),
        migrations.AddField(
            model_name='article',
            name='attitude',
            field=models.TextField(choices=[('Раздел 1', 'Раздел 1'), ('Раздел 2', 'Раздел 2'), ('Раздел 3', 'Раздел 3'), ('Раздел 4', 'Раздел 4'), ('Раздел 5', 'Раздел 5'), ('Раздел 6', 'Раздел 6'), ('Раздел 7', 'Раздел 7'), ('Авторы', 'Авторы'), ('Томас Пинчон', 'Томас Пинчон'), ('Другое', 'Другое'), ('Запланированные мероприятия', 'Запланированные мероприятия'), ('Записи встреч', 'Записи встреч'), ('Другие книги', 'Другие книги')], default=1, verbose_name='Отношение к разделу'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата'),
        ),
        migrations.AddField(
            model_name='article',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка к статье'),
        ),
        migrations.AddField(
            model_name='article',
            name='sort',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Сортировка'),
        ),
    ]