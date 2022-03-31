import sys
import json
my_settings = open('my_settings.json')
settings = json.load(my_settings)
sys.path.append(settings["BASE_PATH"])


import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import src.get_server_data as gsd
import src.scrape_crypto_table as gct

dag = DAG(
    dag_id='run_daily_jobs',
    description='This dag handles all the jobs which are supposed to run every day',
    schedule_interval='0 1 * * *',
    start_date=datetime.datetime(2022, 3, 29),
    )


run_get_crypto_server_data = PythonOperator(
    task_id = 'run_get_crypto_server_data',
    python_callable= gsd.GetServerData(url=settings["BASE_URL"]).run,
    dag=dag
)

run_scrape_crypto_server_data = PythonOperator(
    task_id = 'run_scrape_crypto_server_data',
    python_callable= gct.ScrapeCryptoTable().run,
    dag=dag
)

run_get_crypto_server_data >> run_scrape_crypto_server_data