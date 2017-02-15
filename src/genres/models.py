from django.db import models
from django.utils.translation import ugettext as _


class Genres(models.Model):

    name = models.CharField(verbose_name=_('Name'), max_length=255)

    class Meta:
        verbose_name = _('Genre')
        verbose_name_plural = _('Genres')

