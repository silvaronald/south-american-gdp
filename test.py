import pymysql

connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='password',
            database='gdp_sa'
        )

print(connection.cursor())