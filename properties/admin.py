from django.contrib import admin
from .models import Property, ApartmentAttributes, VillaAttributes, \
    HomeAttributes, OfficeAttributes, BuildingAttributes, \
    TownhouseAttributes, ShopAttributes, GarageAttributes


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('agent', 'property_type',)


@admin.register(ApartmentAttributes)
class ApartmentAttributesAdmin(admin.ModelAdmin):
    list_display = ('property', 'property_agent')

    def property_agent(self, obj):
        return obj.property.agent

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'property':
            kwargs['queryset'] = Property.objects.filter(
                property_type=Property.PropertyType.APARTMENT
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(VillaAttributes)
class VillaAttributesAdmin(admin.ModelAdmin):
    list_display = ('property', 'property_agent')

    def property_agent(self, obj):
        return obj.property.agent

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'property':
            kwargs['queryset'] = Property.objects.filter(
                property_type=Property.PropertyType.VILLA
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(HomeAttributes)
class HomeAttributesAdmin(admin.ModelAdmin):
    list_display = ('property', 'property_agent')

    def property_agent(self, obj):
        return obj.property.agent

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'property':
            kwargs['queryset'] = Property.objects.filter(
                property_type=Property.PropertyType.HOME
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(OfficeAttributes)
class OfficeAttributesAdmin(admin.ModelAdmin):
    list_display = ('property', 'property_agent')

    def property_agent(self, obj):
        return obj.property.agent

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'property':
            kwargs['queryset'] = Property.objects.filter(
                property_type=Property.PropertyType.OFFICE
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(BuildingAttributes)
class BuildingAttributesAdmin(admin.ModelAdmin):
    list_display = ('property', 'property_agent')

    def property_agent(self, obj):
        return obj.property.agent

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'property':
            kwargs['queryset'] = Property.objects.filter(
                property_type=Property.PropertyType.BUILDING
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(TownhouseAttributes)
class TownhouseAttributesAdmin(admin.ModelAdmin):
    list_display = ('property', 'property_agent')

    def property_agent(self, obj):
        return obj.property.agent

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'property':
            kwargs['queryset'] = Property.objects.filter(
                property_type=Property.PropertyType.TOWNHOUSE
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(ShopAttributes)
class ShopAttributesAdmin(admin.ModelAdmin):
    list_display = ('property', 'property_agent')

    def property_agent(self, obj):
        return obj.property.agent

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'property':
            kwargs['queryset'] = Property.objects.filter(
                property_type=Property.PropertyType.SHOP
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(GarageAttributes)
class GarageAttributesAdmin(admin.ModelAdmin):
    list_display = ('property', 'property_agent')

    def property_agent(self, obj):
        return obj.property.agent

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'property':
            kwargs['queryset'] = Property.objects.filter(
                property_type=Property.PropertyType.GARAGE
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
