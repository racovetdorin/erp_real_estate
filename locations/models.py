from django.db import models
from django.utils.translation import gettext as _
from softdelete.models import SoftDeleteObject


class Country(SoftDeleteObject):
    name = models.CharField(max_length=256, verbose_name=_('Country name'))
    code = models.CharField(blank=True, max_length=10,
                            help_text=_('Country code (two characters)'))

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
        ordering = ['name']

    def __str__(self):
        return self.name


class City(SoftDeleteObject):

    class Type(models.TextChoices):
        CITY = 'city', _('City')
        COMMUNE = 'commune', _('Commune')
        VILLAGE = 'village', _('Village')

    name = models.CharField(max_length=256, verbose_name=_('City name'))
    country = models.ForeignKey(Country, blank=True, null=True, related_name='cities',
                                on_delete=models.SET_NULL)
    type = models.CharField(max_length=50, db_index=True, choices=Type.choices, default=Type.CITY,
                            blank=True)

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')
        ordering = ['name']

    def __str__(self):
        if self.country:
            return f'{self.name} ({self.country})'
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=256, verbose_name=_('Street name'))
    city = models.ForeignKey(City, blank=True, null=True, verbose_name=_('City'),
                             related_name='streets', on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _('Street')
        verbose_name_plural = _('Streets')
        ordering = ['name']

    def __str__(self):
        if self.city:
            return f'{self.name} ({self.city})'
        return self.name
