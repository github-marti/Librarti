from django.forms import ModelForm, TextInput, Textarea
from .models import Book, Review

class BookForm(ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'author', 'image', 'synopsis')
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'author': TextInput(attrs={'class': 'form-control'}),
            'image': TextInput(attrs={'class': 'form-control'}),
            'synopsis': Textarea(attrs={'class': 'form-control'})
            }

class ReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = ('stars', 'thoughts')
        widgets = {
            'thoughts': Textarea(attrs={'class': 'form-control'})
        }