from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class GenresConfig(AppConfig):
    name = 'genres'
    verbose_name = _('Genres')
