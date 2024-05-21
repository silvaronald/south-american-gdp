from utils.country import Country
import requests

class API():
    def __init__(self) -> None:
        self.BASE_URL = 'https://api.worldbank.org/v2'
        self.ENDPOINT = '/countries/ARG;BOL;BRA;CHL;COL;ECU;GUY;PRY;PER;SUR;URY;VEN/indicator/NY.GDP.MKTP.CD'
        self.params = {
            'format': 'json',
            'date': '2019:2023',
            'per_page': 5,
            'page': 1
        }

    def get_countries_gdp(self):
        countries = []

        while True:
            response = requests.get(self.BASE_URL + self.ENDPOINT, params=self.params)

            if response.status_code == 200:
                data = response.json()[1]

                if len(data) < self.params['per_page']:
                    break
                
                country = Country()

                country.id = data[0]['country']['id']
                country.iso3code = data[0]['countryiso3code']
                country.name = data[0]['country']['value']

                for row in data:
                    year = row['date']
                    gdp_value = row['value']

                    if gdp_value:
                        gdp_value /= 10**9 # Convert to billions

                    country.gdp[year] = gdp_value
                
                countries.append(country)

                self.params['page'] += 1

            else:
                raise(Exception(f"Failed to retrieve data: {response.status_code}"))
        
        self.params['page'] = 1

        return countries