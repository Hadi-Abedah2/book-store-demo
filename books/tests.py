from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from .models import Book, Review
# Create your tests here.


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user( # new
            username="reviewuser",
            email="reviewuser@email.com",
            password="testpass123",
        )

        cls.special_permission = Permission.objects.get(
        codename="special_status"
        ) 

        cls.book = Book.objects.create(
            title="Harry Potter",
            author="JK Rowling",
            price="25.00",
        )

        cls.reviews = Review.objects.create(
            book=cls.book,
            review='Awesome',
            author=cls.user
        )
    
    def test_book_listing(self):
        self.assertEqual(self.book.__str__(), "Harry Potter")
        self.assertEqual(f"{self.book.title}", "Harry Potter")
        self.assertEqual(f"{self.book.author}", "JK Rowling")
        self.assertEqual(f"{self.book.price}", "25.00") 

    def test_book_list_view_for_logged_in_user(self):
        self.client.login(email="reviewuser@email.com", password="testpass123")
        resp = self.client.get(reverse("book_list"))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(Book.objects.all().count(), 1)
        self.assertContains(resp, "Harry Potter")
        self.assertTemplateUsed(resp, "books/book_list.html")


    def test_book_list_view_for_logged_out_user(self): # new
        self.client.logout()
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 302) # new
        self.assertRedirects(
        response, "%s?next=/books/" % (reverse("account_login")))
        response = self.client.get(
        "%s?next=/books/" % (reverse("account_login")))
        self.assertContains(response, "Log In")


    def test_book_detail_view_with_permissions(self): # new
        self.client.login(email="reviewuser@email.com", password="testpass123")
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Harry Potter")
        self.assertContains(response, "Awesome")
        self.assertTemplateUsed(response, "books/book_detail.html")
