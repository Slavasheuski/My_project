# Generated by Django 4.0.10 on 2023-07-26 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artiles_authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Имя и фамилия автора')),
                ('date_of_birthday', models.DateTimeField(verbose_name='Дата рождения')),
                ('date_of_death', models.DateTimeField(verbose_name='Дата смерти')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
    ]