import sys
from geopy.distance import great_circle
from geopy.geocoders import Nominatim

geolocator = Nominatim()

# Set units, miles by default
if len(sys.argv) > 1:
    if sys.argv[1] in ['mi', 'mile', 'miles']:
        UNIT = 'miles'
    if sys.argv[1] in ['km', 'kilometer', 'kilometers']:
        UNIT = 'kilometers'
    if "--optimize" in sys.argv:
        OPTIMIZE = True
else:
    UNIT = 'miles'

def distanceBetweenCities(city1, city2, units):
    location1 = geolocator.geocode(city1)
    coord1 = (location1.latitude, location1.longitude)
    location2 = geolocator.geocode(city2)
    coord2 = (location2.latitude, location2.longitude)
    if units == 'miles':
        return great_circle(coord1, coord2).miles
    elif units == 'kilometers':
        return great_circle(coord1, coord2).kilometers

totalDistance = 0
distances = []

# Populate list of cities via STDIN
cities = []
prompt = "Enter a city, enter a blank to finish: \n"
city = input(prompt)
while city != "":
    cities.append(city)
    city = input(prompt)

numCities = len(cities)

if numCities < 2:
    print("Please enter more than one city, exiting")
else:
    # Create itinerary
    prev = cities[0]
    for c in cities[1:]:
        distance = distanceBetweenCities(prev, c, UNIT)
        totalDistance += distance
        distances.append(distance)

    print("Success! Your vacation itinerary is:\n")

    for i in range(len(distances)):
        print("    " + str(cities[i]) + " -> " + str(cities[i+1]) + ": " + str(distances[i]))

    print("\nTotal distance covered in your trip: " + str(totalDistance) + " " + UNIT)


