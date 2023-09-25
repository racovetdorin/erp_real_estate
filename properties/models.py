from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import gettext as _
from softdelete.models import SoftDeleteObject


class Property(SoftDeleteObject):
    class PropertyType(models.TextChoices):
        APARTMENT = 'apartment', _('Apartment')
        VILLA = 'villa', _('Villa')
        HOME = 'home', _('Home')
        OFFICE = 'office', _('Office')
        BUILDING = 'building', _('Building')
        TOWNHOUSE = 'townhouse', _('Townhouse')
        SHOP = 'shop', _('Shop')
        GARAGE = 'garage', _('Garage')

    agent = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.SET_NULL,
                              related_name='properties', verbose_name=_('Agent'))
    property_type = models.CharField(blank=True, null=True, choices=PropertyType.choices,
                                     verbose_name=_('Property Type'), max_length=30)

    class Meta:
        indexes = [models.Index(fields=['property_type'],)]

    @property
    def attributes(self):
        type = self.property_type

        property_attributes = {
            Property.PropertyType.APARTMENT: ApartmentAttributes,
            Property.PropertyType.VILLA: VillaAttributes,
            Property.PropertyType.HOME: HomeAttributes,
            Property.PropertyType.OFFICE: OfficeAttributes,
            Property.PropertyType.BUILDING: BuildingAttributes,
            Property.PropertyType.TOWNHOUSE: TownhouseAttributes,
            Property.PropertyType.SHOP: ShopAttributes,
            Property.PropertyType.GARAGE: GarageAttributes
        }

        return property_attributes[type].objects.filter(property=self)


class BasePropertyAttributes(SoftDeleteObject):

    class UnitsOfMeasure(models.TextChoices):
        SQUARE_METERS = 'square_meters', _('Square meters')
        ACRES = 'acres', _('Acres')
        HECTARES = 'hectares', _('Hectares')

    title = models.CharField(max_length=256, null=True, blank=True,
                             verbose_name=_('Property title'))
    description = models.TextField(max_length=3000, blank=True, null=True,
                                   verbose_name=_('Description public'))
    surface_total = models.FloatField(null=True, blank=True, verbose_name=_('Surface total'))
    units_of_measure = models.CharField(max_length=50, blank=True, null=True,
                                        choices=UnitsOfMeasure.choices,
                                        default=UnitsOfMeasure.SQUARE_METERS,
                                        verbose_name=_('Units of measure')
                                        )
    rooms_number = models.IntegerField(choices=((x, x) for x in range(0, 21)), default=0,
                                       verbose_name=_('Rooms number'))
    bathrooms_number = models.IntegerField(choices=((x, x) for x in range(0, 11)), default=0,
                                           verbose_name=_('Bathrooms number'))

    class Meta:
        abstract = True


class ApartmentAttributes(BasePropertyAttributes):
    property = models.OneToOneField(Property, null=True, on_delete=models.SET_NULL,
                                    related_name='apartment_attributes',
                                    verbose_name=_('Apartment attributes'))

    class Meta:
        verbose_name = _('Apartment attributes')
        verbose_name_plural = _('Apartments attributes')
        ordering = ['title']


@receiver(pre_save, sender=ApartmentAttributes)
def pre_save_apartment_attributes(sender, instance, *args, **kwargs):
    if instance.property and instance.property.property_type != Property.PropertyType.APARTMENT:
        raise ValidationError('Property type must be apartment!')


class VillaAttributes(BasePropertyAttributes):
    property = models.ForeignKey(Property, on_delete=models.CASCADE,
                                 related_name='villa_attributes',
                                 verbose_name=_('Villa attributes'))

    class Meta:
        verbose_name = _('Villa attributes')
        verbose_name_plural = _('Villas attributes')
        ordering = ['title']


@receiver(pre_save, sender=VillaAttributes)
def pre_save_villa_attributes(sender, instance, *args, **kwargs):
    if instance.property.property_type != Property.PropertyType.VILLA:
        raise ValidationError('Property type must be villa!')


class HomeAttributes(BasePropertyAttributes):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='home_attributes',
                                 verbose_name=_('Home attributes'))

    class Meta:
        verbose_name = _('Home attributes')
        verbose_name_plural = _('Homes attributes')
        ordering = ['title']


@receiver(pre_save, sender=HomeAttributes)
def pre_save_home_attributes(sender, instance, *args, **kwargs):
    if instance.property.property_type != Property.PropertyType.HOME:
        raise ValidationError('Property type must be home!')


class OfficeAttributes(BasePropertyAttributes):
    property = models.ForeignKey(Property, on_delete=models.CASCADE,
                                 related_name='office_attributes',
                                 verbose_name=_('Office attributes'))

    class Meta:
        verbose_name = _('Office attributes')
        verbose_name_plural = _('Offices attributes')
        ordering = ['title']


@receiver(pre_save, sender=OfficeAttributes)
def pre_save_office_attributes(sender, instance, *args, **kwargs):
    if instance.property.property_type != Property.PropertyType.OFFICE:
        raise ValidationError('Property type must be office!')


class BuildingAttributes(BasePropertyAttributes):
    property = models.ForeignKey(Property, on_delete=models.CASCADE,
                                 related_name='building_attributes',
                                 verbose_name=_('Building attributes'))

    class Meta:
        verbose_name = _('Building attributes')
        verbose_name_plural = _('Buildings attributes')
        ordering = ['title']


@receiver(pre_save, sender=BuildingAttributes)
def pre_save_building_attributes(sender, instance, *args, **kwargs):
    if instance.property.property_type != Property.PropertyType.BUILDING:
        raise ValidationError('Property type must be building!')


class TownhouseAttributes(BasePropertyAttributes):
    property = models.ForeignKey(Property, on_delete=models.CASCADE,
                                 related_name='townhouse_attributes',
                                 verbose_name=_('Townhouse attributes'))

    class Meta:
        verbose_name = _('Townhouse attributes')
        verbose_name_plural = _('Townhouses attributes')
        ordering = ['title']


@receiver(pre_save, sender=TownhouseAttributes)
def pre_save_townhouse_attributes(sender, instance, *args, **kwargs):
    if instance.property.property_type != Property.PropertyType.TOWNHOUSE:
        raise ValidationError('Property type must be townhouse!')


class ShopAttributes(BasePropertyAttributes):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='shop_attributes',
                                 verbose_name=_('Shop attributes'))

    class Meta:
        verbose_name = _('Shop attributes')
        verbose_name_plural = _('Shops attributes')
        ordering = ['title']


@receiver(pre_save, sender=ShopAttributes)
def pre_save_shop_attributes(sender, instance, *args, **kwargs):
    if instance.property.property_type != Property.PropertyType.SHOP:
        raise ValidationError('Property type must be shop!')


class GarageAttributes(BasePropertyAttributes):
    property = models.ForeignKey(Property, on_delete=models.CASCADE,
                                 related_name='garage_attributes',
                                 verbose_name=_('Garage attributes'))
    rooms_number = None
    bathrooms_number = None

    class Meta:
        verbose_name = _('Garage attributes')
        verbose_name_plural = _('Garages attributes')
        ordering = ['title']


@receiver(pre_save, sender=GarageAttributes)
def pre_save_garage_attributes(sender, instance, *args, **kwargs):
    if instance.property.property_type != Property.PropertyType.GARAGE:
        raise ValidationError('Property type must be garage!')
