from multiprocessing import Pool, cpu_count
from functools import partial


def square(y, addition_component, x):
    return x ** y + addition_component


num_processes = 4
comparison_list = [1, 2, 3]
power = 3
addition_component = 2
num_cpu_to_use = max(1, cpu_count() - 1)

print('Number of cpus being used:', num_cpu_to_use)

partial_function = partial(square, power, addition_component)

with Pool(num_cpu_to_use) as mp_pool:
    result = mp_pool.map(partial_function, comparison_list)

print(result)