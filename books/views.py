from typing import Any
from django.shortcuts import render
from django.views import generic
from .models import Book
# Create your views here.


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'   # I can omit this since it follows the naming convention.



class BookDetailView(generic.DetailView):
    model = Book 
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        book = Book.objects.get(pk=self.kwargs.get('pk'))
        reviews = book.reviews.all()
        context = {'book':book, 'reviews':reviews}
        return context