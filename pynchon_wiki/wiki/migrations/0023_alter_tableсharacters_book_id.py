# Generated by Django 3.2.16 on 2024-04-09 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0022_auto_20240405_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tableсharacters',
            name='book_id',
            field=models.ForeignKey(choices=[(1, 'Радуга тяготения'), (2, 'V')], on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='wiki.book', verbose_name='Книга'),
        ),
    ]
