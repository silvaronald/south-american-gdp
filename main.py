from api import API
from database_handler import DatabaseHandler

def main():
    countries = API().get_countries_gdp()

    db = DatabaseHandler()

    db.insert_countries(countries)
    db.insert_gdps(countries)

    db.select_countries_gdps()
main()