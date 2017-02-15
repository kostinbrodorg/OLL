from django.contrib import admin
from authors.models import Author


class AdminAuthor(admin.ModelAdmin):
    pass

admin.site.register(Author, AdminAuthor)
