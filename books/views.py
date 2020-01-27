from django.shortcuts import render, get_object_or_404
from .models import Book
from django.urls import reverse
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'books/index.html'
    context_object_name = 'latest_books_list'

    def get_queryset(self):
        """Return the last five books according to add date"""
        return Book.objects.order_by('-add_date')[:5]

class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'