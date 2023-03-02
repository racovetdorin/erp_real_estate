from django.db import models
from django.utils.translation import gettext as _
from erp.models import TimeStampedModel


class Property(TimeStampedModel):
    class PropertyType(models.TextChoices):
        APARTMENT = 'apartment', _('Apartment')
        HOUSE = 'house', _('House')
        OFFICE = 'office', _('Office')
        LAND = 'land', _('Land')
        COMMERCIAL = 'commercial', _('Commercial')
        INDUSTRIAL = 'industrial', _('Industrial')
        HOTEL = 'hotel', _('Hotel')
        SPECIAL_PROPERTY = 'special_property', _('Special Property')

    agent = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.SET_NULL, related_name='properties',
                              verbose_name=_('Agent'))
    property_type = models.CharField(blank=True, null=True, choices=PropertyType.choices,
                                     verbose_name=_('Property Type'), max_length=30)

    class Meta:
        indexes = [models.Index(fields=['property_type'],)]
