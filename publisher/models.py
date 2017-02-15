from django.db import models
from django.utils.translation import ugettext as _


class Publisher(models.Model):

    name = models.CharField(verbose_name=_('Name'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Publisher')
        verbose_name_plural = _('Publishers')
