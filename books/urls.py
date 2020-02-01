from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('book/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('book/new/', views.new_book, name='new_book'),
    path('book/<int:book_id>/delete', views.delete_book, name='delete_book'),
    path('book/<int:book_id>/edit_book', views.update_book, name='update_book'),
    path('book/<int:book_id>/edit_review', views.update_review, name='update_review'),
    path('books/search/', views.SearchResultsView.as_view(), name='results'),
    path('books/browse/by_<str:order_by>', views.BrowseView.as_view(), name='order_by')
]