from django.shortcuts import render, redirect
from .models import Artiles_authors, Books
from .forms import ArtilesFormAuthors, BooksForm


def authors_home(request):
    authors = Artiles_authors.objects.order_by('title')
    return render(request, 'authors/authors_home.html', {'authors': authors})

def books_home(request):
    books = Books.objects.all()
    return render(request, 'authors/books_home.html', {'books': books})

def create_authors(request):
    error = ''
    if request.method == 'POST':
        form = ArtilesFormAuthors(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ArtilesFormAuthors()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'authors/create_authors.html', data)


def create_books(request):
    create_author() # добавляем начальные данные для компаний
    error = ''

    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = BooksForm()

    authors = Artiles_authors.objects.all()

    return render(request, 'authors/create_books.html', {'authors': authors, 'form': form, 'error': error})

def create_author():
    if Artiles_authors.objects.all().count() == 0:
        Artiles_authors.objects.create(title="Достоевский", date_of_birthday="1821-11-11", date_of_death="1881-02-09")
        Artiles_authors.objects.create(title="Пушкин", date_of_birthday="1799-06-06", date_of_death="1837-02-10")
        Artiles_authors.objects.create(title="Лермантов", date_of_birthday="1814-10-15", date_of_death="1841-07-27")
