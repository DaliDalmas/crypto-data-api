from bs4 import BeautifulSoup
import pickle

import logging as lg
lg.basicConfig(level=lg.INFO)
HANDLE = 'scrape-server-data'
LOGGER = lg.getLogger(HANDLE)


class ScrapeCryptoTable:

    def __init__(self):
        self.cryptotable:list = []
        self.html_docs:list = []

    def _extract_data_from_page(self, soup):
        # TBD
        pass

    def scrape_server_data(self)->None:
        for page in self.html_docs:
            page_soup = BeautifulSoup(page, 'html.parser')
            self._extract_data_from_page(page_soup)
            break
        LOGGER.info('Done Scraping')
        return None

    def import_server_data(self):
        with open ('fetched_server_data', 'rb') as fetched_data:
            self.html_docs = pickle.load(fetched_data)
        LOGGER.info('Scraped data imported')

    def run(self):
        self.import_server_data()
        self.scrape_server_data()

if __name__=='__main__':
    cryptotable = ScrapeCryptoTable()
    cryptotable.run()
    # LOGGER.info(cryptotable.html_docs)