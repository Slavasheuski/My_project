from django.test import TestCase

from .models import Artiles_authors, Books

class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Artiles_authors.objects.create(title="Пушкин", date_of_birthday="1799-06-06", date_of_death="1837-02-10")

    def test_title_label(self):
        author=Artiles_authors.objects.get(id=1)
        field_label = author._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'Имя и фамилия автора')

    def test_date_of_birthday_label(self):
        author=Artiles_authors.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birthday').verbose_name
        self.assertEquals(field_label,'Дата рождения')
    
    def test_date_of_death_label(self):
        author=Artiles_authors.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label,'Дата смерти')

    def test_title_max_length(self):
        author=Artiles_authors.objects.get(id=1)
        max_length = author._meta.get_field('title').max_length
        self.assertEquals(max_length,50)



class BooksModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Books.objects.create(title="Мцыри", author=Artiles_authors.objects.create(title="Пушкин", date_of_birthday="1799-06-06", date_of_death="1837-02-10"), date="2020-06-06")

    def test_title_label(self):
        author=Books.objects.get(id=1)
        field_label = author._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'Название книги')

    def test_date_label(self):
        author=Books.objects.get(id=1)
        field_label = author._meta.get_field('date').verbose_name
        self.assertEquals(field_label,'Дата публикации')

    def test_title_max_length(self):
        author=Books.objects.get(id=1)
        max_length = author._meta.get_field('title').max_length
        self.assertEquals(max_length,50)
