import requests
from bs4 import BeautifulSoup
from io import StringIO
import pandas as pd

class WebScraper:
    
    def __init__(self):
        pass
    
    @staticmethod
    def grab_html(url, parser='lxml'):
        html = requests.get(url, headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}).text
        # create soup of html
        soup = BeautifulSoup(html, parser)
        return soup
    
    @staticmethod
    def find_table(soup):
        table_element = soup.find('table')
        df = pd.read_html(StringIO(str(table_element)))[0].set_index('Date') # use index as date for each entry of stock data.
        return df