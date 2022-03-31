import sys
import json
my_settings = open('my_settings.json')
settings = json.load(my_settings)
sys.path.append(settings["BASE_PATH"])

from datetime import datetime
from time import sleep
import requests
import pickle


import logging as lg
lg.basicConfig(level=lg.INFO)
HANDLE = 'get-server-data'
LOGGER = lg.getLogger(HANDLE)

class GetServerData:
    def __init__(self, url:str):
        self.page:int = 0
        self.html_docs:list = []
        self.url:str = url

    def fetch_server_data(self)->None:
        while self.page <= 300:
            self.page += 1 
            try:
                LOGGER.info(f'Fetching page {self.page} . . .')
                doc = requests.get(self.url+f'?page={self.page}').content
            except Exception as e:
                LOGGER.info(f'Calling server {self.url}  stopped at {datetime.now()} on page {self.page}')
                LOGGER.info(e)
                return None
            self.html_docs.append(doc)
 
    def run(self):
        self.fetch_server_data()
        with open(settings["BINARY_SERVER_DATA_PATH"], 'wb') as fetched_server_data:
            pickle.dump(self.html_docs, fetched_server_data)

if __name__=='__main__':
    server_data = GetServerData(url=settings["BASE_URL"])
    server_data.run()