from .models import Artiles_authors, Books
from django.forms import ModelForm, TextInput, DateInput, ModelChoiceField, SelectMultiple


class ArtilesFormAuthors(ModelForm):
    class Meta:
        model = Artiles_authors
        fields = ['title', 'date_of_birthday', 'date_of_death']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя автора'
            }),
            'date_of_birthday': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения'
            }),
            'date_of_death': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата смерти'
            })
        }



class BooksForm(ModelForm):

    authors = Artiles_authors.objects.all()
    author = ModelChoiceField(queryset = Artiles_authors.objects.all(), empty_label = "Выберите автора")

    class Meta:
        model = Books
        fields = ['title', 'author', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название произведения'
            }),
            'date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            })
        }