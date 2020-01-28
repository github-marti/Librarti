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

def update(request, book_id, column):
    book = get_object_or_404(Book, pk=book_id)

    # for synopsis updates
    if column == 'synopsis':
        try:
            book.synopsis = request.POST[column]
        except (KeyError):
            return render(request, 'books/detail.html', {
                'book': book,
                'error_message': "Synopsis not successfully saved."
            })
        else:
            book.save()
            return HttpResponseRedirect(reverse('books:detail', args=(book.id,)))
    
    # for review updates
    elif column == 'review':
        try:
            book.review = request.POST[column]
        except (KeyError):
            return render(request, 'books/detail.html', {
                'book': book,
                'error_message': "Review not successfully saved."
            })
        else:
            book.save()
            return HttpResponseRedirect(reverse('books:detail', args=(book.id,)))