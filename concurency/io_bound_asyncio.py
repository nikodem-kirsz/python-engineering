import asyncio
import time
import aiohttp
import requests
# without session 27 seconds
# with session 13 seconds
# session & threading version took 2 seconds, with task per request
# requests & threading version on 5 workers = 6,26 seconds, 6 workers processing requests from pool
# session & asyncio version took 0.75 seconds, task per request ( tasks = len(sites))
# multiprocessing (running on 8 cores on CPU) took 2,19 seconds
# multiprocessing (running on 30 processes and 8 cores on CPU) took 1,11 seconds

async def download_site(session, url):
    async with aiohttp.request.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))

async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))

    duration = time.time() - start_time
    print(f"Download {len(sites)} in {duration} seconds")