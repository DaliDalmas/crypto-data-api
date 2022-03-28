from bs4 import BeautifulSoup


class GenerateCryptoTable:

    def __init__(self, html_docs:list):
        self.cryptotable
        self.html_docs:list = html_docs

    def scrape_server_data(self)->None:
        for html_doc in self.html_docs:
            self.html_soup = BeautifulSoup(html_doc,'html.parser')
        return None