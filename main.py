import time

from workers.WikiWorker import WikiWorker
from workers.YahooFinanceWorkers import YahooFinacePriceWorker


def main():
    scraper_start_time = time.time()

    wikiWorker = WikiWorker()
    current_workers = []
    for symbol in wikiWorker.get_sp_500_companies():
        yahooFinacePriceWorker = YahooFinacePriceWorker(symbol=symbol)
        current_workers.append(yahooFinacePriceWorker)

    for i in range(len(current_workers)):
        current_workers[i].join()

    print('Extracting time took:', round(time.time() - scraper_start_time, 1))


if __name__ == "__main__":
    main()
