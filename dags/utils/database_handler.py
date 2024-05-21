from utils.country import Country

class DatabaseHandler:
    def __init__(self, connection) -> None:
        self.connection = connection

    @staticmethod
    def get_query(query):
        with open(f'database/{query}.sql', 'r') as file:
            return(file.read())

    def insert_countries(self, countries):
        insert_query = self.get_query('insert_country')

        with self.connection.cursor() as cursor:
            for country in countries:
                cursor.execute(insert_query, (country.id, country.name, country.iso3code))
        
        self.connection.commit()

    def insert_gdps(self, countries):
        insert_query = self.get_query('insert_gdps')

        with self.connection.cursor() as cursor:
            for country in countries:
                for year, value in country.gdp.items():
                    cursor.execute(insert_query, (country.id, int(year), value))
        
        self.connection.commit()

    def select_countries_gdps(self):
        select_query = self.get_query('select_countries_gdps')
        
        with self.connection.cursor() as cursor:
            cursor.execute(select_query)

            column_names = [d[0] for d in cursor.description]
            
            print('---'.join(column_names))
            
            rows = cursor.fetchall()

            for row in rows:
                print('---'.join(map(str, row)))