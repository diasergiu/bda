from faker import Faker
from concurrent.futures import ThreadPoolExecutor
import threading
import time


fake = Faker()
counter_lock = threading.Lock()

def start_execution(worker_name: str, number_of_sentences: int):
    phrase = generate_phrase(number_of_sentences)
    save_phrase_to_file(worker_name, phrase)

def generate_phrase(number_of_sentences: int):
    listPhrases = []
    for _ in range(number_of_sentences):
        listPhrases.append(fake.sentence(nb_words=6))
    return listPhrases

def save_phrase_to_file(worker_name : str, phrase ,  file_name = "phrases.txt"):
    with counter_lock:  
        with open(file_name, "a") as f:
            for p in phrase:
                f.write(f"{worker_name}: {p}\n")

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=10) as executor:
        for i in range(10):
            executor.submit(start_execution, f"Worker {i+1}", 10)
              