from datetime import datetime
from time import sleep
import requests

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
        while self.page < 329:
            self.page += 1 
            try:
                LOGGER.info(f'Fetching page {self.page} . . .')
                doc = requests.get(self.url+f'?page={self.page}').content
            except Exception as e:
                LOGGER.info(f'Calling server {self.url}  stopped at {datetime.now()} on page {self.page}')
                LOGGER.info(e)
                return None
            self.html_docs.append(doc)
            sleep(1)
 
    def run(self)->str:
        self.fetch_server_data()

if __name__=='__main__':
    server_data = GetServerData(url='https://www.coinbase.com/price').run()
    print(server_data.html_docs)