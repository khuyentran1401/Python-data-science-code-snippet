# pip install geopy

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='find_location')
location = geolocator.geocode('30 North Circle Drive, Edwardsville, IL')

print(location.address)
# 30, Circle Drive, Edwardsville, Madison County, Illinois, 62025, United States

print(location.latitude, location.longitude)
# 38.80371599362934 -89.93842706888563