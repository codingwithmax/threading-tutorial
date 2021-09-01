from multiprocessing import Pool, cpu_count


def square(x, y):
    return x ** y


num_processes = 4
comparison_list = [1, 2, 3]
power_list = [4, 5, 6]

num_cpu_to_use = max(1, cpu_count() - 1)

print('Number of cpus being used:', num_cpu_to_use)

prepared_list = []
for i in range(len(comparison_list)):
    prepared_list.append((comparison_list[i], power_list[i]))
print('List to use as input:', prepared_list)
with Pool(num_cpu_to_use) as mp_pool:
    result = mp_pool.starmap(square, prepared_list)  # [(1, 4), (2 ,5), (3, 6)]

print(result)