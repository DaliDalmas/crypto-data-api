import sys
sys.path.append('/Users/dalmas.otieno/Documents/learnings/crypto-data-api-and-analytics-dashboard')

import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import get_server_data as gsd
import scrape_crypto_table as gct

dag = DAG(
    dag_id='run_daily_jobs',
    description='This dag handles all the jobs which are supposed to run every day',
    schedule_interval='0 1 * * *',
    start_date=datetime.datetime(2022, 3, 29),
    )


run_get_crypto_server_data = PythonOperator(
    task_id = 'run_get_crypto_server_data',
    python_callable= gsd.GetServerData(url='https://www.coinbase.com/price').run,
    dag=dag
)

run_scrape_crypto_server_data = PythonOperator(
    task_id = 'run_scrape_crypto_server_data',
    python_callable= gct.ScrapeCryptoTable().run,
    dag=dag
)

run_get_crypto_server_data >> run_scrape_crypto_server_data