from multiprocessing import Process, Queue
import time


def check_value_in_list(x, i, number_of_processes, queue):
    max_number_to_check_to = 10**8
    lower = int(i * max_number_to_check_to / number_of_processes)
    upper = int((i + 1) * max_number_to_check_to / number_of_processes)
    number_of_hits = 0
    for i in range(lower, upper):
        if i in x:
            number_of_hits += 1

    queue.put((lower, upper, number_of_hits))


num_processes = 4
comparison_list = [1, 2, 3]
queue = Queue()
start_time = time.time()
processes = []
for i in range(num_processes):
    t = Process(target=check_value_in_list, args=(comparison_list, i, num_processes, queue))
    processes.append(t)

for t in processes:
    t.start()

for t in processes:
    t.join()

queue.put('DONE')

while True:
    v = queue.get()
    if v == 'DONE':
        break
    lower, upper, number_of_hits = v
    print('Between', lower, 'and', upper, 'we have', number_of_hits,'values in the list')

print('Everything took:', time.time() - start_time, 'seconds')
