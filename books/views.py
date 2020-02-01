from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Book, Review
from .forms import BookForm, ReviewForm, StarForm

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'books/book_view.html'
    context_object_name = 'books_list'

    def get_queryset(self):
        """Return the last five books according to add date"""
        return Book.objects.order_by('-add_date')[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['star_form'] = StarForm()
        return context

class BrowseView(generic.ListView):
    template_name = 'books/browse.html'
    context_object_name = 'ordered_books'

    def get_queryset(self):
        order_by = self.kwargs['order_by']
        if order_by == 'stars':
            return Book.objects.order_by('review__stars')
        else:
            return Book.objects.order_by(order_by)

class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'

class SearchResultsView(generic.ListView):
    book_model = Book
    template_name = 'books/search_results.html'
    context_object_name = 'search_results'

    def get_queryset(self):
        if 'title' in self.request.GET:
            query = self.request.GET.get('title')
            return Book.objects.filter(title__icontains=query) 
        elif 'author' in self.request.GET:
            query = self.request.GET.get('author')
            return Book.objects.filter(author__icontains=query)
        else:
            query = self.request.GET.get('stars')
            return Book.objects.filter(review__stars=query)

def new_book(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        review_form = ReviewForm(request.POST)
        if book_form.is_valid():
            book = book_form.save(commit=False)
            book.add_date = timezone.now()
            book.save()
            review = review_form.save(commit=False)
            review.book = book
            review.save()
            return redirect('books:detail', pk=book.pk)       
    else:
        book_form = BookForm()
        review_form = ReviewForm()
    return render(request, 'books/book_edit.html', {
        'book_form': book_form,
        'review_form': review_form
    })

def update_book(request, book_id):
    instance = get_object_or_404(Book, id=book_id)
    form = BookForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            book = form.save()
            return redirect('books:detail', pk=book.pk)
    else:
        return render(request, 'books/book_edit.html', {'book_form': form, 'book_id': book_id})

def update_review(request, book_id):
    instance = get_object_or_404(Review, book=book_id)
    form = ReviewForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            review = form.save()
            return redirect('books:detail', pk=review.book.pk)
    else:
        return render(request, 'books/book_edit.html', {'review_form': form, 'book_id': book_id})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    try:
        book.delete()
    except:
        print("Book not deleted successfully")
    else:
        return redirect('books:index')