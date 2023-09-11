import asyncio

async def coroutine1():
    for _ in range(3):
        await asyncio.sleep(1)
        print("Coroutine 1 running on event loop 1")

async def coroutine2():
    for _ in range(3):
        await asyncio.sleep(1)
        print("Coroutine 2 running on event loop 2")

async def main():
    # Create two event loops
    loop1 = asyncio.new_event_loop()
    loop2 = asyncio.new_event_loop()

    # Create tasks for coroutine1 and coroutine2 on their respective event loops
    asyncio.set_event_loop(loop1)
    tasks1 = [
        asyncio.create_task(coroutine1()),
        asyncio.create_task(coroutine1()),
    ]

    asyncio.set_event_loop(loop2)
    tasks2 = [
        asyncio.create_task(coroutine2()),
        asyncio.create_task(coroutine2()),
    ]

    # Use asyncio.gather() to run tasks on different event loops
    results1 = await asyncio.gather(*tasks1)
    results2 = await asyncio.gather(*tasks2)

    # Close event loops
    loop1.close()
    loop2.close()

if __name__ == "__main__":
    asyncio.run(main())
