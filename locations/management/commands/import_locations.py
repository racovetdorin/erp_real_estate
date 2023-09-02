import csv
from django.core.management.base import BaseCommand
from locations.models import Country, City


class Command(BaseCommand):
    def handle(self, **options):
        with open('./locations_csv/worldcountries.csv', 'r', newline='') as countries_csv:
            csv_reader = csv.reader(countries_csv)
            for row in csv_reader:
                Country.objects.get_or_create(
                    code=row[0],
                    name=row[1]+'/'+row[0]
                )
        with open('./locations_csv/worldcities.csv', 'r', newline='') as cities_csv:
            csv_reader = csv.reader(cities_csv)
            for row in csv_reader:
                try:
                    print(row, 19)
                    country = Country.objects.get(name__startswith=row[4], code=row[5])
                    city, created = City.objects.get_or_create(name=row[1], country=country)
                    print(city, '---', created)
                except Country.DoesNotExist:
                    print(row, 24)
