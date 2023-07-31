from django.db import models

class Artiles_authors(models.Model):
    title = models.CharField('Имя и фамилия автора', max_length=50)
    date_of_birthday = models.DateField('Дата рождения', null=True, blank=True)
    date_of_death = models.DateField('Дата смерти', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Books(models.Model):
    title = models.CharField('Название книги', max_length=50)
    author = models.ForeignKey(Artiles_authors, on_delete=models.CASCADE)
    date = models.DateField('Дата публикации', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'