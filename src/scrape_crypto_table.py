import sys
import json
my_settings = open('my_settings.json')
settings = json.load(my_settings)
sys.path.append(settings["BASE_PATH"])

from bs4 import BeautifulSoup
import pickle
import pandas as pd


import logging as lg
lg.basicConfig(level=lg.INFO)
HANDLE = 'scrape-server-data'
LOGGER = lg.getLogger(HANDLE)


class ScrapeCryptoTable:

    def __init__(self):
        self.data_titles:list = ["coin_name", "coin_value"]
        self.cryptodata:list = []
        self.html_docs:list = []

    def _extract_data_from_page(self, soup)->None:
        table_body = soup.find('tbody')
        if table_body is None:
            return None
        table_rows = table_body.find_all('tr')
        for row in table_rows:
            coin_name_soup = row.find('p', {'class': 'iworPT'})
            coin_value_soup = row.find('div', {'class':['sc-131di3y-0', 'cLgOOr']})
            if coin_name_soup is None:
                continue
            coin_name = coin_name_soup.text
            coin_value = coin_value_soup.text
            self.cryptodata.append([coin_name, coin_value])

    def scrape_server_data(self)->None:
        for page in self.html_docs:
            page_soup = BeautifulSoup(page, 'html.parser')
            self._extract_data_from_page(page_soup)
        LOGGER.info('Done Scraping')
        return None

    def import_server_data(self)->None:
        with open (settings["BINARY_SERVER_DATA_PATH"], 'rb') as fetched_data:
            self.html_docs = pickle.load(fetched_data)
        LOGGER.info('Scraped data imported')
    
    def save_csv_to_disk(self):
        dataframe = pd.DataFrame(self.cryptodata)
        dataframe.columns = self.data_titles
        dataframe.to_csv(settings["CSV_SERVER_DATA_PATH"], index=False)
        LOGGER.info('Scraped data saved to disk')

    def run(self)->None:
        self.import_server_data()
        self.scrape_server_data()
        self.save_csv_to_disk()

if __name__=='__main__':
    cryptotable = ScrapeCryptoTable()
    cryptotable.run()