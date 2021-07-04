import time

from multiprocessing import Queue

from workers.WikiWorker import WikiWorker
from workers.YahooFinanceWorkers import YahooFinancePriceScheduler


def main():
    symbol_queue = Queue()
    scraper_start_time = time.time()

    wikiWorker = WikiWorker()
    yahoo_finance_price_scheduler_threads = []
    num_yahoo_finance_price_workers = 4
    for i in range(num_yahoo_finance_price_workers):
        yahooFinancePriceScheduler = YahooFinancePriceScheduler(input_queue=symbol_queue)
        yahoo_finance_price_scheduler_threads.append(yahooFinancePriceScheduler)

    for symbol in wikiWorker.get_sp_500_companies():
        symbol_queue.put(symbol)

    for i in range(len(yahoo_finance_price_scheduler_threads)):
        symbol_queue.put('DONE')

    for i in range(len(yahoo_finance_price_scheduler_threads)):
        yahoo_finance_price_scheduler_threads[i].join()

    print('Extracting time took:', round(time.time() - scraper_start_time, 1))


if __name__ == "__main__":
    main()
