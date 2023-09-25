# from functools import partial
from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent='my_app')
# geocode = partial(geolocator.geocode, languages='ro')
location = geolocator.geocode('strada Mihai Viteazul 104, Ialoveni')
print(location.address)
print(location.latitude, location.longitude)

loc_by_cords = geolocator.reverse('46.9351817, 28.778219550000003')
print(loc_by_cords.address)
