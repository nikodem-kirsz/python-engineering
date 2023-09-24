import asyncio
import random

"""
Received data point: 89
Received data point: 20
Received data point: 90
Received data point: 4
Received data point: 91
Received data point: 90
Received data point: 43
Received data point: 60
Received data point: 71
Received data point: 60
"""

# Async generator yielding values based on the randomized number 
# and consumer waiting and reading async data
async def async_data_stream():
    for _ in range(10):
        await asyncio.sleep(random.uniform(0.1, 1.0))  # Simulate varying delays
        data = random.randint(1, 100)
        yield data

async def consume_async_data_stream():
    async for data_point in async_data_stream():
        print(f"Received data point: {data_point}")

async def main():
    await consume_async_data_stream()

if __name__ == "__main__":
    asyncio.run(main())

# Event messaging with asyncio.Queue broadcasting and receiving messages
async def async_data_stream(queue: asyncio.Queue()):
    for _ in range(10):
        await asyncio.sleep(random.uniform(0.1, 1.0))
        data = random.randint(1, 100)
        print(f"Broadcasting {data} into the queue.")
        await queue.put(data)

async def consume_async_data_stream(queue: asyncio.Queue()):
    while True:
        data_point = await queue.get()
        print(f"Received data point: {data_point}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    producer_task = asyncio.create_task(async_data_stream(queue))
    consumer_task = asyncio.create_task(consume_async_data_stream(queue))
    
    await asyncio.gather(producer_task)

    await queue.join()

    consumer_task.cancel()

if __name__ == "__main__":
    asyncio.run(main())