from django.apps import AppConfig

from django.utils.translation import ugettext_lazy as _


class AuthorsConfig(AppConfig):
    name = 'authors'
    verbose_name = _('Authors')
