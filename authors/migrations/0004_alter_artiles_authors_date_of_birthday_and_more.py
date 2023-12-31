# Generated by Django 4.0.10 on 2023-07-27 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0003_remove_books_name_books_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artiles_authors',
            name='date_of_birthday',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='artiles_authors',
            name='date_of_death',
            field=models.DateField(verbose_name='Дата смерти'),
        ),
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authors.artiles_authors'),
        ),
        migrations.AlterField(
            model_name='books',
            name='date',
            field=models.DateField(verbose_name='Дата публикации'),
        ),
    ]
