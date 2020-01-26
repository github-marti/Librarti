from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.
def index(request):
    latest_book_list = Book.objects.order_by('-add_date')[:5]
    output = ', '.join(['{} by {}'.format(q.title, q.author) for q in latest_book_list])
    return HttpResponse(output)
