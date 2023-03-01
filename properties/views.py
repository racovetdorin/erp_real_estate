from django.shortcuts import render
from .models import Property


def index(request):
    # properties = Property.objects.select_related('agent').all()
    # for prop in properties:
    #     temp = prop.agent.email

    return render(request, 'properties/index.html')
