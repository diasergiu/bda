import multiprocessing as mp
import random
import time

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


def generate_and_sort_numbers(n=10000):
    numbers = [random.random() for _ in range(n)]
    bubble_sort(numbers)

def serial_runner(runs=3):
    start = time.perf_counter()

    # TODO: call generate_and_sort_numbers() runs times
    generate_and_sort_numbers()
    generate_and_sort_numbers()
    generate_and_sort_numbers()

    end = time.perf_counter()
    return end - start

def parallel_runner(runs=3):
    start = time.perf_counter()

    processes = []

    # TODO: create runs processes
    # with mp.Pool(3) as pool:
    #     result = pool.map(generate_and_sort_numbers, [10000, 10000, 10000])
    #     print(result)
    result1 = mp.Process(target=generate_and_sort_numbers)
    result2 = mp.Process(target=generate_and_sort_numbers)  
    result3 = mp.Process(target=generate_and_sort_numbers)
    # TODO: start each process
    result1.start()
    result2.start()
    result3.start()
    # TODO: wait for each process to finish
    result1.join()
    result2.join()
    result3.join()

    end = time.perf_counter()
    return end - start

def parallel_runner_pool(runs=3):
    start = time.perf_counter()

    processes = []

    # TODO: create runs processes
    with mp.Pool(3) as pool:
        result = pool.map(generate_and_sort_numbers, [10000, 10000, 10000])
        print(result)

    # TODO: start each process

    # TODO: wait for each process to finish

    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    serial_time = serial_runner(runs=3)
    parallel_time = parallel_runner(runs=3)
    parallel_pool_time = parallel_runner_pool(runs=3)

    print(f"Serial time: {serial_time:.2f}s")
    print(f"Parallel time: {parallel_time:.2f}s")
    print(f"Parallel pool time: {parallel_pool_time:.2f}s")