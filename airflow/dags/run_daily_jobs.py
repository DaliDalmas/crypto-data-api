import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from ...get_server_data import GetServerData

dag = DAG(
    dag_id='run_daily_jobs',
    description='This dag handles all the jobs which are supposed to run every day',
    schedule_interval='0 1 * * *',
    start_date=datetime.datetime(2022, 3, 29),
    )

PythonOperator(
    task_id = 'run_get_crypto_server_data',
    python_callable= GetServerData(url='https://www.coinbase.com/price').run(),
    dag=dag
)
