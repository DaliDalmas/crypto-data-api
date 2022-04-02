import sys
import json
my_settings = open('my_settings.json')
settings = json.load(my_settings)
sys.path.append(settings["BASE_PATH"])

import pandas as pd
from sqlalchemy import create_engine
import psycopg2 as pg
import psycopg2.extras
import datetime

class LoadDataToDB:
    def __init__(self, host:str, user:str, passw:str, db:str, schema:str) -> None:
        self.host:str = host
        self.user = user
        self.passw:str = passw
        self.db:str = db
        self.schema:str = schema
        self.table:str = None
        self.data = None

    def read_csv(self, data_path:str, table:str):
        self.table = table
        self.data = pd.read_csv(data_path)

    def save_to_table(self):
        conn = pg.connect(
            host=self.host,
            database=self.db,
            user=self.user,
            password=self.passw
            )

        self.data['coin_value'] = self.data['coin_value']\
            .apply(lambda value: str(value).replace('$','').replace(',',''))

        self.data['coin_value'] = pd.to_numeric(
            self.data['coin_value'],
            errors='coerce')
        self.data['date_time'] = datetime.datetime.now()
        if len(self.data) > 0:
            df_columns = list(self.data)
            columns = ",".join(df_columns)
            values = "VALUES({})".format(",".join(["%s" for _ in df_columns])) 
            insert_stmt = f"INSERT INTO {self.schema}.{self.table} ({columns}) {values}"
            cur = conn.cursor()
            pg.extras.execute_batch(cur, insert_stmt, self.data.values)
            conn.commit()
            cur.close()

    def run(self):
        self.read_csv(
            data_path=settings['table_details']['csv_path'],
            table=settings['table_details']['table']
            )
        self.save_to_table()


if __name__=='__main__':
    load_data = LoadDataToDB(
        host=settings['database']['host'],
        user=settings['database']['user'],
        passw=settings['database']['passwor'],
        db=settings['database']['db'],
        schema=settings['database']['schema']
    )
    load_data.run()
