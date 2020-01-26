from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    latest_book_list = Book.objects.order_by('-add_date')[:5]
    context = {
        'latest_book_list': latest_book_list
    }
    return render(request, 'books/index.html', context)