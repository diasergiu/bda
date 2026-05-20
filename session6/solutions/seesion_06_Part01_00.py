# import threading

# lock = threading.Lock()

# with lock:
#     # only one thread can run this block at a time
#     print("safe shared work")

# second example

# from concurrent.futures import ThreadPoolExecutor
# import threading
# import time


# counter = 0
# counter_lock = threading.Lock()


# def add_one(worker_name):
#     global counter

#     print(f"{worker_name} is waiting for the lock")

#     with counter_lock:
#         print(f"{worker_name} entered the critical section")

#         current_value = counter
#         time.sleep(0.5)
#         counter = current_value + 1

#         print(f"{worker_name} updated counter to {counter}")


# if __name__ == "__main__":
#     with ThreadPoolExecutor(max_workers=4) as executor:
#         executor.submit(add_one, "Worker A")
#         executor.submit(add_one, "Worker B")
#         executor.submit(add_one, "Worker C")
#         executor.submit(add_one, "Worker D")

#     print(f"Final counter value: {counter}")


# third example


from faker import Faker

fake = Faker()

def generate_phrase():
    return fake.sentence(nb_words=6)

print(generate_phrase())