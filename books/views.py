from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.views import generic
from .models import Book, Review
from .forms import ReviewForm
# Create your views here.


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    template_name = 'books/book_list.html'   # I can omit this since it follows the naming convention.
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        search = self.request.GET.get('s')
        if search:
            query_set = Book.objects.filter(Q(title__icontains=search) | Q(author__icontains=search))
            return query_set

        else : 
            return super().get_queryset()

class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book 
    #permission_required = "books.special_status"

    def get_queryset(self) -> QuerySet[Any]:
        query_set = Book.objects.all().prefetch_related('reviews__author',) 
        return query_set

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data()
        review_form = ReviewForm()
        context['review_form'] = review_form
        return context 
    


class ReviewCreateView(LoginRequiredMixin, generic.CreateView):
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
    

    