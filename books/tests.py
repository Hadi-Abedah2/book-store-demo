from django.test import TestCase
from django.urls import reverse
from .models import Book
# Create your tests here.


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.book = Book.objects.create(
            title="Harry Potter",
            author="JK Rowling",
            price="25.00",
        )
    
    def test_book_listing(self):
        self.assertEqual(self.book.__str__(), "Harry Potter")
        self.assertEqual(f"{self.book.title}", "Harry Potter")
        self.assertEqual(f"{self.book.author}", "JK Rowling")
        self.assertEqual(f"{self.book.price}", "25.00") 

    def test_book_list_view(self):
        resp = self.client.get(reverse("book_list"))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(Book.objects.all().count(), 1)
        self.assertContains(resp, "Harry Potter")
        self.assertTemplateUsed(resp, "books/book_list.html")

    def test_book_detail_view(self):
        resp = self.client.get(self.book.get_absolute_url())
        no_resp = self.client.get("/books/12345/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(no_resp.status_code, 404)
        self.assertContains(resp, "Harry Potter")
        self.assertTemplateUsed(resp, "books/book_detail.html")