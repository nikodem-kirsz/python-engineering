import asyncio

async def future():
    await asyncio.sleep(3)
    return "Awaited"

async def past():
    await asyncio.sleep(-3)
    return "Get to the past"

async def main():
    loop1 = asyncio.new_event_loop()
    loop2 = asyncio.new_event_loop()
    loop3 = asyncio.new_event_loop()

    # Assign coroutines to separate event loops
    asyncio.set_event_loop(loop1)
    tasks1 = [
        asyncio.create_task(future()),
        asyncio.create_task(future()),
        asyncio.create_task(future()),
        asyncio.create_task(future()),
    ]
    
    asyncio.set_event_loop(loop2)
    tasks2 = [
        asyncio.create_task(past()),
        asyncio.create_task(future()),
        asyncio.create_task(future()),
    ]

    asyncio.set_event_loop(loop3)
    tasks3 = [
        asyncio.create_task(past()),
        asyncio.create_task(future()),
        asyncio.create_task(future()),
    ]
    single_task2 = await future()
    print(f"single_task: {single_task2}")

    single_task = await asyncio.create_task(past())
    print(f"single_task: {single_task}")

    single_task2 = await asyncio.create_task(future())
    print(f"single_task: {single_task2}")

    # Use asyncio.gather() to await the completion of tasks
    results1 = await asyncio.gather(*tasks1)
    print(f"Results1: {results1}")

    results2 = []
    # Use of as_completed not to wait for all of them
    for res in asyncio.as_completed(tasks2):
        compl = await res
        print(f"Results2 item: {compl}")
        results2.append(compl)

    results3 = await asyncio.gather(*tasks3)
    print(f"Results3: {results3}")

    loop1.close()
    loop2.close()
    loop3.close()
    
    return [results1, results2, results3]

if __name__ == "__main__":
    # Run main in event loop
    result = asyncio.run(main())
    print("Result", result)