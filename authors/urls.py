from django.urls import path
from . import views

urlpatterns = [
    path('', views.authors_home, name="authors_home"),
    path('books_home', views.books_home, name="books_home"),
    path('create_authors', views.create_authors, name="create_authors"),
    path('create_books', views.create_books, name="create_books")
]