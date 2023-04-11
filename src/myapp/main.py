import requests
from geopy.geocoders import GeoNames
from geopy.exc import GeocoderTimedOut
from haversine import haversine
import pypopulation
from mpl_toolkits.basemap import Basemap
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

import geopandas as gpd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import contextily as ctx
import pycountry

# find smallest numbers 
from heapq import nsmallest
import time


def get_country_name(lat, lon):
    """
    Given a latitude and longitude, returns the name of the country
    using the Nominatim API.
    """
    url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=jsonv2"
    headers = {'accept-language': 'en-US'}
    # url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
    response = requests.get(url, headers=headers).json()
    print(response)
    # print(response["address"]["country"])
    return response["address"]["country"]


def get_capital(country):
    url = f"https://restcountries.com/v3.1/translation/{country}"
    response = requests.get(url).json()
    # list
    # print(type(response[0]["capitalInfo"]["latlng"]))
    # print(response)
    # print(response[0]["capital"])
    # print(response[2]["capital"])
    return response[0]["capital"]

def get_altitude(lat, lon):
    url = f"https://api.opentopodata.org/v1/etopo1?locations={lat},{lon}"
    response = requests.get(url).json()

    #{'results': [{'dataset': 'etopo1', 'elevation': 122.0, 'location': {'lat': 48.0, 'lng': 23.0}}], 'status': 'OK'}
    print("elevation", response["results"][0]["elevation"])
    return response["results"][0]["elevation"]

def get_coord_capital(country):
    url = f"https://restcountries.com/v3.1/translation/{country}"
    response = requests.get(url).json()
    # return list, but must tuple for calculate distance
    # print(type(response[0]["capitalInfo"]["latlng"]))
    # list to tuple
    coord = tuple(response[0]["capitalInfo"]["latlng"])
    # print(coord)
    return coord
    # return capital

def get_distance_inpPoint_capital(inputPoint_tuple, capital_tuple):
    haversine_distance = haversine(inputPoint_tuple, capital_tuple)
    # print(haversine_distance)
    return haversine_distance

def get_population(country):
    url = f"https://restcountries.com/v3.1/translation/{country}"
    response = requests.get(url).json()
    print(response[0]["cca2"])
    country_code = response[0]["cca2"]
    population = pypopulation.get_population(country_code)
    # print(population)
    return population

def three_nearest_country(input_coord):
    # iterate throught all countries
    nearest_capital = []
    nearest_distance = []
    start_time = time.time()
    for country in pycountry.countries:

        country_name = country.name
        # print(country_name)
        # get_capital(country_name)
        if not country_name:
            continue
        
        try:
            coord = get_coord_capital(country_name)
            # latitude, longitude = coord
            distance = get_distance_inpPoint_capital(input_coord, coord) 
            # distance = ((latitude - lat) ** 2 + (longitude - lon) ** 2) ** 0.5

            nearest_capital.append(country_name)
            nearest_distance.append(distance)

        except KeyError:
            pass
    nearest_capitals = [capital for _, capital in nsmallest(3, zip(nearest_distance, nearest_capital))]
    print(nearest_capitals)
    end_time = time.time()
    total_time = end_time - start_time
# 138.35876393318176
    print("Execution time:", total_time, "seconds")
    return nearest_capitals


def check_coordinates(latitude, longitude):
    if -90 <= latitude <= 90 and -180 <= longitude <= 180:
        return True
    else:
        return False
    

## China
# lat = 39.9042
# lon = 116.4074
# lat = 48.9226
# lon = 24.7111

# if check_coordinates(lat, lon):
#     print("Valid coordinates.")

# input_coord = (lat, lon)

# country = get_country_name(lat, lon)
# print('---------------')
# capital = get_capital(country)
# print(*capital)
# ## +
# altitude = get_altitude(lat, lon)
# print("=====")
# coord_capital = get_coord_capital(country)

# distance = get_distance_inpPoint_capital(input_coord, coord_capital)

# population = get_population(country)

# country = three_nearest_country()
# import folium



# # Send a request to the OpenStreetMap API to obtain the country's GeoJSON file
# url = f'https://nominatim.openstreetmap.org/reverse.php?format=geojson&lat={lat}&lon={lon}'
# response = requests.get(url)
# geojson = response.json()

# # Create a folium map centered on the point
# m = folium.Map(location=[lat, lon], zoom_start=10)

# # Add the country's polygon to the map
# folium.GeoJson(data=geojson).add_to(m)

# # Display the map
# m
