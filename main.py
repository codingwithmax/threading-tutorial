import time

from workers.SleepyWorkers import SleepyWorker
from workers.SquaredSumWorkers import SquaredSumWorker


def main():
    calc_start_time = time.time()

    current_workers = []
    for i in range(5):
        maximum_value = (i + 1) * 1000000
        squaredSumWorker = SquaredSumWorker(n=maximum_value)
        current_workers.append(squaredSumWorker)

    for i in range(len(current_workers)):
        current_workers[i].join()

    print('Calculating sum of squares took:', round(time.time() - calc_start_time, 1))

    sleep_start_time = time.time()

    current_workers = []
    for seconds in range(1, 6):
        sleepyWorker = SleepyWorker(seconds=seconds)
        current_workers.append(sleepyWorker)

    for i in range(len(current_workers)):
        current_workers[i].join()

    print('sleep took:', round(time.time() - sleep_start_time, 1))


if __name__ == "__main__":
    main()
