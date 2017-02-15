"""
Library Author Model
"""

from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import ugettext as _

from genres.models import Genres
from publisher.models import Publisher


class Author(models.Model):

    """
    Author model, describe author properties
    """

    name = models.CharField(verbose_name=_('Author Name'), max_length=255, blank=False, null=False)
    slug = models.SlugField(max_length=255)
    nickname = models.CharField(verbose_name=_('Nickname'), max_length=255)
    country = CountryField(verbose_name=_('Country'))
    date_of_birth = models.DateField(verbose_name=_('Date of Birth'))
    date_of_death = models.DateField(verbose_name=_('Date ot Death'), blank=True)
    genres = models.ManyToManyField(Genres, verbose_name=_('Genres'))
    publishers = models.ManyToManyField(Publisher, verbose_name=_('Publishers'))

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')

