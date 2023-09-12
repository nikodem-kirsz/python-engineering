import asyncio

"""
There’s a subtlety to this pattern: if you don’t await t within main(), 
it may finish before main() itself signals that it is complete. 
Because asyncio.run(main()) calls loop.run_until_complete(main()), 
"""
async def coro(seq) -> list:
    await asyncio.sleep(max(seq))
    return list(reversed(seq))

async def main():
     # This is a bit redundant in the case of one task
     # We could use `await coro([3, 2, 1])` on its own
    t = asyncio.create_task(coro([3,2,1]))
    print(asyncio.all_tasks())
    await t
    print(f't: type {type(t)}')
    print(f't done: {t.done()}')

a = asyncio.run(main())
print(a)

import time

async def main():
    t = asyncio.create_task(coro([3,2,1]))
    t2 = asyncio.create_task(coro([10,5,0]))
    print('Start:', time.strftime('%X'))
    a = await asyncio.gather(t, t2)
    print('End:', time.strftime('%X'))  # Should be 10 seconds
    print(f'Both tasks done: {all((t.done(), t2.done()))}')
    return a

a = asyncio.run(main())
print(a)
"""
Start: 00:19:07
End: 00:19:17
Both tasks done: True
"""

async def main():
    t1 = asyncio.create_task(coro([3,2,1]))
    t2 = asyncio.create_task(coro([10,5,0]))
    print('Start:', time.strftime('%X'))
    for res in asyncio.as_completed((t1, t2)):
        compl = await res
        print(f'res: {compl} completed at {time.strftime("%X")}')
    print('End:', time.strftime('%X'))
    print(f'Both tasks done: {all((t1.done(), t2.done()))}')    

a = asyncio.run(main())
print(a)
"""
Start: 00:19:17
res: [1, 2, 3] completed at 00:19:20
res: [0, 5, 10] completed at 00:19:27
End: 00:19:27
"""
    