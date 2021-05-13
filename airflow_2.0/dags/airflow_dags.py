from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime, timedelta
import time
from datetime import datetime
import pandas
from sqlalchemy import create_engine
import psycopg2

#test123
default_args = {
    'owner': 'solee',
    'depends_on_past': False,
    'start_date': datetime(2020, 6, 3),
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(dag_id='test',
          default_args=default_args,
          schedule_interval="@once",
          )

def _sleep():
    for i in range(100):
        print(str(datetime.now()))
        time.sleep(1)


wait_this = PythonOperator(
    task_id='wait',
    python_callable=_sleep,
    dag=dag,
)


task = PythonOperator(
    task_id=f'test',
    python_callable=_sleep,
    dag=dag,
)


[wait_this, task]