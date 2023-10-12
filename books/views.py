from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.views import generic
from .models import Book, Review
from .forms import ReviewForm
# Create your views here.


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'   # I can omit this since it follows the naming convention.



class BookDetailView(generic.DetailView):
    model = Book 
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        book = Book.objects.get(pk=self.kwargs.get('pk'))
        reviews = book.reviews.all()
        review_form = ReviewForm()
        context = {'book':book, 'reviews':reviews, 'review_form':review_form}
        return context 
    


class ReviewCreateView(generic.CreateView):
    model = Review
    form_class  = ReviewForm 
    #success_url = reverse_lazy('book_list')
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.book = Book.objects.get(pk=self.kwargs.get('pk'))
        self.object = form.save()
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('book_detail', kwargs={'pk': self.kwargs.get('pk')})
    

    