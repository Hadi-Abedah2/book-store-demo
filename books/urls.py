from django.urls import path
from .views import BookListView, BookDetailView, ReviewCreateView




urlpatterns = [

    path("", BookListView.as_view(), name="book_list"),
    path("<uuid:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("<uuid:pk>/review/new", ReviewCreateView.as_view(), name="review_create"),

]
