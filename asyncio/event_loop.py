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
    loop2.set_debug(True)

    # Assign coroutines to separate event loops
    asyncio.set_event_loop(loop)
    results1 = await asyncio.gather(future(), future(), past(), future())
    asyncio.set_event_loop(loop2)
    results2 = await past()

    print(results1)
    print(results2)
    
    loop.close()
    loop2.close()
    return [results1, results2]

if __name__ == "__main__":
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

    # Run coroutine1 on the first event loop
    asyncio.set_event_loop(loop1)
    loop1.run_until_complete(coroutine1())

    # Run coroutine2 on the second event loop
    asyncio.set_event_loop(loop2)
    loop2.run_until_complete(coroutine2())

    # Close the event loops
    loop1.close()
    loop2.close()

if __name__ == "__main__":
    main()    