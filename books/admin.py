from django.contrib import admin
from .models import Book, Review

# Define an inline admin descriptor for Review model
# which acts a bit like a singleton
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1  # how many rows to show

# Define the admin class
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]
    list_display = ('title', 'author', 'price')

# Register the Admin classes for Review using the decorator
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'review', 'author')  # or any fields in your Review model
