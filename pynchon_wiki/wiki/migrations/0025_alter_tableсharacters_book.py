# Generated by Django 3.2.16 on 2024-04-09 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0024_rename_book_id_tableсharacters_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tableсharacters',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='wiki.book', verbose_name='Книга'),
        ),
    ]
