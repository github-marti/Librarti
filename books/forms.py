from django import forms
from .models import Book, Review

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'author', 'synopsis',)