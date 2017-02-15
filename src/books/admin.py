from django.contrib import admin
from books.models import Book


class AdminBooks(admin.ModelAdmin):
    pass

admin.site.register(Book, AdminBooks)
