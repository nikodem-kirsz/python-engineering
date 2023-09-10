import requests
import multiprocessing
import time

# without session 27 seconds
# with session 13 seconds
# session & threading version took 2 seconds, with task per request
# requests & threading version on 5 workers = 6,26 seconds, 6 workers processing requests from pool
# session & asyncio version took 0.75 seconds, task per request ( tasks = len(sites))
# multiprocessing (running on 8 processes and 8 cores on CPU) took 2,19 seconds
# multiprocessing (running on 30 processes and 8 cores on CPU) took 1,11 seconds

session = None

def set_global_session():
    global session
    if not session:
        session = requests.Session()

def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}: Read {len(response.content)} from {url}")

def download_all_sites(sites):
    with multiprocessing.Pool(processes=30, initializer=set_global_session) as pool:
        pool.map(download_site, sites)
        
if __name__ == '__main__':
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
