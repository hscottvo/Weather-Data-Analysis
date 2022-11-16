from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps


def test():
    print("Hello world")
    owm = OWM("fdcc86acf4e1025e275556082759b630")


default_args = {"owner": "scott", "retries": 5, "retry_delay": timedelta(minutes=2)}

with DAG(
    dag_id="our_first_dag_v5",
    default_args=default_args,
    description="This is our first dag that we write",
    start_date=datetime(2021, 7, 29, 2),
    schedule_interval="@daily",
) as dag:

    task1 = PythonOperator(task_id="test", python_callable=test)
    task1
