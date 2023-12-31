from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView
# Create your tests here.

class HomepageTests(SimpleTestCase):

    def setUp(self) -> None:
        self.response = self.client.get(reverse("home"))

    def test_url_exists_at_correct_location(self): 
        self.assertEqual(self.response.status_code, 200)
    

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_does_contain_incorrect_html(self):
        self.assertContains(self.response, "home page")
    
    def test_homepage_does_not_contain_incorrect_html(self): # new
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_hompepage_url_resolves_homepage_view(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTests(SimpleTestCase):

    def setUp(self):
        self.response = self.client.get(reverse("about"))
    
    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)


    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, "about.html")

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, "About Page")

    def test_aboutpage_url_resolves_aboutpage_view(self):
        view = resolve("/about/")
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)