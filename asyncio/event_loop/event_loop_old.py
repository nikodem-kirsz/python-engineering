import asyncio

async def coroutine1():
    print("Coroutine 1 started")
    await asyncio.sleep(2)
    print("Coroutine 1 finished")

async def coroutine2():
    print("Coroutine 2 started")
    await asyncio.sleep(1)
    print("Coroutine 2 finished")

def main():
    # Create the first event loop
    loop1 = asyncio.new_event_loop()

    # Create the second event loop
    loop2 = asyncio.new_event_loop()

    # It has to be set due to main not being run in a event loop
    asyncio.set_event_loop(loop1)
    # Use asyncio.ensure_future() to create tasks for the coroutines
    task1 = asyncio.ensure_future(coroutine1())
    task2 = asyncio.ensure_future(coroutine2())
    try:
        loop1.run_until_complete(asyncio.gather(task1, task2))
    finally:
        loop1.close()

    asyncio.set_event_loop(loop2)
    try:
        loop2.run_until_complete(asyncio.gather(coroutine1(), coroutine2()))
    finally:
        loop2.close()

    # Close the event loops
    loop1.close()
    loop2.close()

if __name__ == "__main__":
    # Run a function not in an event loop
    main()    