from django.contrib import admin
from publisher.models import Publisher


class AdminPublisher(admin.ModelAdmin):
    pass

admin.site.register(Publisher, AdminPublisher)
