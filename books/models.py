"""
Library Books models
"""
import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from authors.models import Author
from publisher.models import Publisher
from genres.models import Genres


class Book(models.Model):

    """
    This model describes all books fields
    """

    name = models.CharField(verbose_name=_('Book Name'), max_length=255)
    slug = models.SlugField(max_length=255)
    author = models.OneToOneField(Author, verbose_name=_('Author Name'))
    count = models.IntegerField(verbose_name=_('Book counts'))

    release_date = models.DateField(
        verbose_name=_('Release date'),
        default=datetime.date.today
    )

    release_date_bg = models.DateField(
        verbose_name=_('Release date BG'),
        default=datetime.date.today
    )

    release_by = models.OneToOneField(Publisher, verbose_name=_('Publisher'))

    created_by = models.OneToOneField(
        User,
        verbose_name=_('Created by'),
        related_name='create_by_user'
    )

    create_on = models.DateTimeField(
        verbose_name=_('Created on'),
        auto_now_add=True,
        db_index=True
    )

    update_by = models.OneToOneField(
        User,
        verbose_name=_('Updated by'),
        related_name='update_by_user'
    )

    update_on = models.DateTimeField(
        verbose_name=_('Updated on'), 
        auto_now=True,
        db_index=True
    )

    isbn = models.CharField(verbose_name=_('ISBN'), max_length=255)
    genre = models.OneToOneField(Genres, verbose_name=_('Genres'))
    description = models.TextField(verbose_name=_('Description'))
    is_available = models.BooleanField(verbose_name=_('Is Available?'))
    is_active = models.BooleanField(verbose_name=_('Is Active?'))
    # cover = StdImageField()

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

