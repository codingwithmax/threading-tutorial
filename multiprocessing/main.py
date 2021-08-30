from multiprocessing import Pool, cpu_count


def square(x):
    return x ** 2


num_processes = 4
comparison_list = [1, 2, 3]

num_cpu_to_use = max(1, cpu_count() - 1)

print('Number of cpus being used:', num_cpu_to_use)

with Pool(num_cpu_to_use) as mp_pool:
    result = mp_pool.map(square, comparison_list)

print(result)