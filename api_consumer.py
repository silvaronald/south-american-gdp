import requests
import pandas as pd

class GDP:
    _2019 = None
    _2020 = None
    _2021 = None
    _2022 = None
    _2023 = None

class Country:
    id = None
    name = None
    iso3code = None
    gdp = GDP()

    
# Define the API endpoint and parameters
BASE_URL = 'https://api.worldbank.org/v2'
ENDPOINT = '/countries/ARG;BOL;BRA;CHL;COL;ECU;GUY;PRY;PER;SUR;URY;VEN/indicator/NY.GDP.MKTP.CD'
params = {
    'format': 'json',
    'date': '2019:2023',
    'per_page': 5,
    'page': 1
}

countries = []

while True:
    response = requests.get(BASE_URL + ENDPOINT, params=params)

    if response.status_code == 200:
        data = response.json()[1]

        if len(data) < params['per_page']:
            break
        
        country = Country()

        country.id = data[0]['country']['id']
        country.iso3code = data[0]['countryiso3code']
        country.name = data[0]['country']['value']

        for row in data:
            year = row['date']
            gdp_value = row['value']

            setattr(country.gdp, f'_{year}', gdp_value)

        countries.append(country)

        params['page'] += 1
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        break
