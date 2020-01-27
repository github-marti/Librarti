from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
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

def update_synopsis(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    try:
        book.synopsis = request.POST['synopsis']
    except (KeyError):
        return render(request, 'books/detail.html', {
            'book': book,
            'error_message': "Data not successfully saved."
        })
    else:
        print(book.synopsis)
        book.save()
        return HttpResponseRedirect(reverse('books:detail', args=(book.id,)))