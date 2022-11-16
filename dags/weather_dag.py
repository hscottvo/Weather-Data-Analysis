from datetime import datetime, timedelta
import requests
import pandas as pd

from airflow import DAG
from airflow.operators.python import PythonOperator


def test():
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m"
    )
    # print(response.json())
    out = pd.DataFrame(
        [response.json()["hourly"]["time"], response.json()["hourly"]["temperature_2m"]]
    ).T
    out.columns = ["hour", "temp"]

    out["hour"] = pd.to_datetime(out["hour"])
    print(out.dtypes)
    out.to_csv("output.csv")


default_args = {"owner": "scott", "retries": 5, "retry_delay": timedelta(minutes=2)}

with DAG(
    dag_id="Hourly-Temps",
    default_args=default_args,
    description="Gets hourly temps at a certain lat/long",
    start_date=datetime(2021, 7, 29, 2),
    schedule_interval="@daily",
) as dag:

    task1 = PythonOperator(task_id="test", python_callable=test)
    task1
