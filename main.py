import time

from multiprocessing import Queue

from workers.WikiWorker import WikiWorker
from workers.YahooFinanceWorkers import YahooFinancePriceScheduler
from workers.PostgresWorker import PostgresMasterScheduler


def main():
    symbol_queue = Queue()
    postgres_queue = Queue()
    scraper_start_time = time.time()

    wikiWorker = WikiWorker()
    yahoo_finance_price_scheduler_threads = []
    num_yahoo_finance_price_workers = 4
    for i in range(num_yahoo_finance_price_workers):
        yahooFinancePriceScheduler = YahooFinancePriceScheduler(input_queue=symbol_queue, output_queue=[postgres_queue])
        yahoo_finance_price_scheduler_threads.append(yahooFinancePriceScheduler)

    postgres_scheduler_threads = []
    num_postgres_workers = 2
    for i in range(num_postgres_workers):
        postgresScheduler = PostgresMasterScheduler(input_queue=postgres_queue)
        postgres_scheduler_threads.append(postgresScheduler)

    symbol_counter = 0
    for symbol in wikiWorker.get_sp_500_companies():
        symbol_queue.put(symbol)
        symbol_counter += 1
        if symbol_counter >= 5:
            break

    for i in range(len(yahoo_finance_price_scheduler_threads)):
        symbol_queue.put('DONE')

    for i in range(len(yahoo_finance_price_scheduler_threads)):
        yahoo_finance_price_scheduler_threads[i].join()

    for i in range(len(postgres_scheduler_threads)):
        postgres_scheduler_threads[i].join()

    print('Extracting time took:', round(time.time() - scraper_start_time, 1))


if __name__ == "__main__":
    main()
