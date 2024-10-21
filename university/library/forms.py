from django import forms
from django.template.defaultfilters import default

from .models import Forma, Book


class FormaForm(forms.ModelForm):
    class Meta:
        model = Forma
        fields = ['full_name', 'age', 'phone', 'address']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'count', 'pages', 'book_file']  # Fayl maydoni qo‘shildi



