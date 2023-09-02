from django.contrib import admin
from .models import Country, City


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'type')
    list_filter = ('country',)

# @admin.register(Street)
# class StreetAdmin(admin.ModelAdmin):
#     list_display = ('property', 'property_agent', 'type', 'price')

#     def property_agent(self, obj):
#         return obj.property.agent
