from itertools import cycle
import asyncio

def endless():
    yield from cycle((9,8,7,6))

e = endless()
total = 0
for i in endless():
    print(f"total: {total}")
    if total < 30:
        print(i, end=" ")
        total += i
    else:
        print()
        break

next(e), next(e), next(e)

"""
This is a crucial distinction: neither asynchronous generators nor 
comprehensions make the iteration concurrent. All that they do is 
provide the look-and-feel of their synchronous counterparts, but with 
the ability for the loop in question to give up control to the event 
loop for some other coroutine to run.
"""

async def mygen(u: int = 10):
    i = 0
    while i < u:
        yield 2**i
        i += 1
        await asyncio.sleep(0.1)

async def main():
    g = [i async for i in mygen()]
    f = [j async for j in mygen() if not (j // 3 % 5)]   
    return g, f

g, f = asyncio.run(main())
print(g)
print(f)
      
async def main():
    print("HEllo")
    await asyncio.sleep(1)
    print('World')

routine = main()
asyncio.run(routine)

loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()    