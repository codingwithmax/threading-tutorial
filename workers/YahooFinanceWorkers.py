import threading
import requests
from lxml import html
import time
import random


class YahooFinacePriceWorker(threading.Thread):
    def __init__(self, symbol, **kwargs):
        super(YahooFinacePriceWorker, self).__init__(**kwargs)
        self._symbol = symbol
        base_url = 'https://finance.yahoo.com/quote/'
        self._url = f'{base_url}{self._symbol}'
        self.start()

    def run(self):
        time.sleep(30 * random.random())
        r = requests.get(self._url)
        if r.status_code != 200:
            return
        page_contents = html.fromstring(r.text)
        price = float(page_contents.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]')[0].text)
        print(price)
