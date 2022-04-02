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
import src.load_data_to_db as ldtb
import src.clean_up as cu

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

run_load_scraped_date = PythonOperator(
    task_id = 'run_load_scraped_date',
    python_callable= ldtb.LoadDataToDB(
        host=settings['database']['host'],
        user=settings['database']['user'],
        passw=settings['database']['passwor'],
        db=settings['database']['db'],
        schema=settings['database']['schema']
    ).run,
    dag=dag
)

def clean_up_files():
    clean = cu.CleanUp(
        path=settings['BINARY_SERVER_DATA_PATH']
    )
    clean.run()

    clean = cu.CleanUp(
        path=settings['CSV_SERVER_DATA_PATH']
    )
    clean.run()

run_clean_up = PythonOperator(
    task_id = 'run_clean_up',
    python_callable=clean_up_files,
    dag=dag
)

run_get_crypto_server_data >> run_scrape_crypto_server_data >> run_load_scraped_date >> run_clean_up