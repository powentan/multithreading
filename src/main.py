import random
import time
import threading
import queue

shared_queue = queue.Queue(maxsize=10)

def producer_worker(stop_event: threading.Event, delay: float):
    running_time = 0.0

    while not stop_event.is_set():
        time.sleep(delay)
        running_time += delay
        random_int = random.randint(0, 100)
        print(f'{running_time:.2f}: put a random integer to queue: {random_int}')
        shared_queue.put(random_int)

    print(f'producer_worker terminated')

def consumer_worker(stop_event: threading.Event, delay: float):
    running_time = 0.0

    while not stop_event.is_set():
        time.sleep(delay)
        running_time += delay
        val = shared_queue.get()
        print(f'{running_time:.2f}: get a random integer queue: {val}')
    print(f'consumer_worker terminated')

# create a event for stoping threads
stop_event = threading.Event()

producer_thread = threading.Thread(target=producer_worker, args=(stop_event, 0.1,))
consumer_thread = threading.Thread(target=consumer_worker, args=(stop_event, 0.15,))

# start threads
producer_thread.start()
consumer_thread.start()

# finish after 10 seconds execution
time.sleep(10)
# signal threads to stop
stop_event.set()
producer_thread.join()
consumer_thread.join()

