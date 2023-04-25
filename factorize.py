import time
from multiprocessing import Pool, cpu_count


def factorize(numbers):
    my_list = []
    for number in numbers:
        div = [x for x in range(1, number // 2 + 1) if number % x == 0]
        div.append(number)
        my_list.append(div)
    return my_list


def factorize_synchr(numbers):
    for number in numbers:
        div = [x for x in range(1, number // 2 + 1) if number % x == 0]
        div.append(number)
    return div


def factorize_multi(numbers):
    with Pool(cpu_count()) as pool:
        return pool.map(factorize_synchr, numbers)


numbers = [128, 255, 99999, 10651060]

start_time = time.time()
process = factorize(numbers)
end_time = time.time()
result = end_time - start_time
print(f"Synchronous CPU time: {result}")

start_time = time.time()
process = factorize_multi(numbers)
end_time = time.time()
result = end_time - start_time
print(f"Multiprocessing time: {result}")
