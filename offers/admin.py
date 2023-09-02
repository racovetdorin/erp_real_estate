from django.contrib import admin
from .models import Offer


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('property', 'property_agent', 'type', 'price')

    def property_agent(self, obj):
        return obj.property.agent
