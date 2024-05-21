# South American countries GDPs from 2019 to 2023

## Overview

This project involves a Python script that fetches the GDP data of all South American countries from 2019 to 2023 using the [World Bank's API](https://datahelpdesk.worldbank.org/knowledgebase/articles/898599-indicator-api-queries), The data is stored in a MySQL database and visualized in a CSV-like format. The project utilizes Apache Airflow and Docker Compose to ensure automation and reproducibility.

## Requirements

- Docker
- Docker Compose
  
## Executing the project
1. Clone this repository
2. In the source directory, run ```docker compose up```
3. Go to <a href="http://localhost:8080/" target="_blank">localhost:8080</a> and login using **_airflow_** as username and password
4. The DAG is set to run every 5 minutes, but you may execute it anytime by pressing the _Trigger DAG_ button in the Home page
5. The result of the query will be printed in the logs of the respective DAG run. You can access the logs by clicking on the DAG run in the Airflow interface. ![image](https://github.com/silvaronald/south-american-gdp/assets/52102394/32fbd01e-2d1b-4947-adf4-0f204fc259d7)
