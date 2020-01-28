from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Book, Review
from .forms import BookForm, ReviewForm

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'books/book_view.html'
    context_object_name = 'latest_books_list'

    def get_queryset(self):
        """Return the last five books according to add date"""
        return Book.objects.order_by('-add_date')[:5]

class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'

def new_book(request):
    book_form = BookForm()
    review_form = ReviewForm()
    return render(request, 'books/book_edit.html', {
        'book_form': book_form,
        'review_form': review_form
    })

def update(request, book_id, column):
    book = get_object_or_404(Book, pk=book_id)
    review = get_object_or_404(Review, book=book_id)
    print(review.stars)

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
            review.stars = request.POST[column]
            print(request.POST[column])
        except (KeyError):
            return render(request, 'books/detail.html', {
                'book': book,
                'error_message': "Review not successfully saved."
            })
        else:
            review.save()
            return HttpResponseRedirect(reverse('books:detail', args=(book.id,)))