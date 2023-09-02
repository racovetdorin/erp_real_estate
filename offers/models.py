from django.db import models
from django.utils.translation import gettext as _
from softdelete.models import SoftDeleteObject


class Offer(SoftDeleteObject):
    class Type(models.TextChoices):
        SALE = 'sale', _('Sale')
        RENT = 'rent', _('Rent')

    class Status(models.TextChoices):
        INCOMPLETE = 'incomplete', _('Incomplete')
        ACTIVE = 'active', _('Active')
        TRANSACTED = 'transacted', _('Transacted')
        WITHDRAWN = 'withdrawn', _('Withdrawn')

    type = models.CharField(max_length=56, choices=Type.choices,
                            default=Type.SALE, verbose_name=_('Type'))
    property = models.ForeignKey('properties.Property', related_name='offers',
                                 on_delete=models.CASCADE,
                                 verbose_name=_('Property'))
    price = models.IntegerField(null=True, blank=True, verbose_name=_('Offer price'))
