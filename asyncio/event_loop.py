import asyncio

async def future():
    await asyncio.sleep(3)
    return "Awaited"

async def past():
    await asyncio.sleep(-3)
    return "Get to the past"

async def main():
    loop = asyncio.new_event_loop()
    loop2 = asyncio.new_event_loop()

    # Assign coroutines to separate event loops
    asyncio.set_event_loop(loop)
    tasks1 = [
        asyncio.create_task(future()),
        asyncio.create_task(future()),
        asyncio.create_task(future()),
        asyncio.create_task(future()),
    ]
    
    asyncio.set_event_loop(loop2)
    tasks2 = [asyncio.create_task(past())]

    # Use asyncio.gather() to await the completion of tasks
    results1 = await asyncio.gather(*tasks1)
    results2 = await asyncio.gather(*tasks2)

    loop.close()
    loop2.close()
    
    return [results1, results2]

if __name__ == "__main__":
    # Run main in event loop
    result = asyncio.run(main())
    print("Result", result)

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