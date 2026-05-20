from concurrent.futures import ThreadPoolExecutor
import threading
import time

import requests


call_limit = threading.Semaphore(4)
write_lock = threading.Lock()


def fetch(request_id):
    url = f"https://httpbin.org/delay/1?request={request_id}"
    response = None
    with call_limit:
        response = requests.get(url, timeout=10)
    return response.text
    # TODO: use call_limit to allow only 4 active requests
    # TODO: call requests.get(url, timeout=10)
    # TODO: write one result line to request_results.txt
    ...

def print_result(result, file_name = "request_results.txt"):
    with write_lock:
        with open(file_name, "a") as f:
            f.write(result + "\n")

def thread_execution(request_id):
    result = fetch(request_id)
    print_result(result)

if __name__ == "__main__":
    start = time.perf_counter()

    with ThreadPoolExecutor(max_workers=4) as executor:
        for i in range(40):
            executor.submit(thread_execution, i)
    # TODO: clear request_results.txt
    # TODO: run 40 fetch tasks using ThreadPoolExecutor
    ...

    end = time.perf_counter()
    print(f"Total time: {end - start:.2f}s")