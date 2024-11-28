from django.views.generic import ListView, DetailView
from books.models import Book

class BookListView(ListView):
    model = Book
    template_name = 'geeks_library/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'geeks_library/book_detail.html'
    context_object_name = 'book'
