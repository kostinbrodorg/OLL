from django.contrib import admin
from genres.models import Genres


class AdminGenres(admin.ModelAdmin):
    pass

admin.site.register(Genres, AdminGenres)
# Register your models here.
