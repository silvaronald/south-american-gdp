from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.mysql_hook import MySqlHook
from utils.api import API
from utils.database_handler import DatabaseHandler

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

hook = MySqlHook(mysql_conn_id='mysql_connection')
connection = hook.get_conn()

def main():
    countries = API().get_countries_gdp()
    db = DatabaseHandler(connection=connection)
    db.insert_countries(countries)
    db.insert_gdps(countries)
    db.select_countries_gdps()

with DAG('main_dag', 
         default_args=default_args, 
         schedule_interval=None, 
         catchup=False) as dag:

    run_script = PythonOperator(
        task_id='run_script',
        python_callable=main
    )

    run_script