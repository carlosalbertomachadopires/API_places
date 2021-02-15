import json
import requests
import pandas as pd
from config import api_key
from pprint import pprint
url = "http://api.openweathermap.org/data/2.5/weather"

### Codes for on city temperature location ###

# parameters = {
#     "q": "houston",
#     "units": "imperial",
#     "appid": api_key
# }

# data = requests.get(url, params=parameters).json()
# pprint(data)

# data_temp = data["main"]["temp"]
# pprint(data_temp)

### Codes for multiple locations ###

# def extract_data(data):
#     return {
#         "name": data["name"],
#         "lat": data["coord"]["lat"],
#         "lon": data["coord"]["lon"],
#         "temp_F":data["main"]["temp"]
#     }
 
# cities = ["Paris", "London", "Oslo", "Beijing"]

# cities_results = []

# for city in cities:
#     data = requests.get(url, params={
#         "q": city,
#         "units": "imperial",
#         "appid": api_key
#     }).json()

#     city_result = extract_data(data)
#     cities_results.append(city_result)

# # pprint(cities_results)

# df = pd.DataFrame(cities_results)

# pprint(df)

### Codes for multiple locations using the full related data ###

def extract_data(data):
    return {
        "name": data["name"],
        "lat": data["coord"]["lat"],
        "lon": data["coord"]["lon"],
        "temp_F":data["main"]["temp"]
    }
 
cities = ["Paris", "London", "Oslo", "Beijing"]

all_data_results = []

for city in cities:
    data = requests.get(url, params={
        "q": city,
        "units": "imperial",
        "appid": api_key
    }).json()

    all_data_results.append(data)

# pprint(cities_results)

df2 = pd.DataFrame(all_data_results)
# df2 = pd.json_normalize(all_data_results)
df2 = pd.json_normalize(all_data_results, "weather")

pprint(df2)



