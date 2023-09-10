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
    
