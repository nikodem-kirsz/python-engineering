import requests
import time
import threading
import concurrent.futures
# without session 27 seconds
# with session 13 seconds
# session & threading version took 2 seconds, with task per request
# requests & threading version on 5 workers = 6,26 seconds, 6 workers processing requests from pool
# session & asyncio version took 0.75 seconds, task per request ( tasks = len(sites))
# multiprocessing (running on 8 cores on CPU) took 2,19 seconds
# multiprocessing (running on 30 processes and 8 cores on CPU) took 1,11 seconds

"""

Parallelism consists of performing multiple operations at the same time. 
Multiprocessing is a means to effect parallelism, and it entails spreading 
tasks over a computer’s central processing units (CPUs, or cores). 
Multiprocessing is well-suited for CPU-bound tasks: tightly bound for loops 
and mathematical computations usually fall into this category.

Concurrency is a slightly broader term than parallelism. 
It suggests that multiple tasks have the ability to run in an overlapping manner. (There’s a saying that concurrency does not imply parallelism.)

Threading is a concurrent execution model whereby multiple threads take turns 
executing tasks. One process can contain multiple threads. 

                    Concurency
    (tasks have ability to run in overlapping manner)
                     /
                  *--Parralelism---*
                   /          /
    Multiprocessing(CPU)   Threading(I/O)  
                 
"""
thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session    

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

def download_all_sites(sites):
    # with requests.Session() as session:
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(sites)) as executor:
        executor.map(download_site, sites)

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Download {len(sites)} in {duration} seconds")
    
