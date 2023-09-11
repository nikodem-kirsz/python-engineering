Parallelism consists of performing multiple operations at the same time. 
Multiprocessing is a means to effect parallelism, and it entails spreading 
tasks over a computer’s central processing units (CPUs, or cores). 
Multiprocessing is well-suited for CPU-bound tasks: tightly bound for loops 
and mathematical computations usually fall into this category.

Concurrency is a slightly broader term than parallelism. 
It suggests that multiple tasks have the ability to run in an overlapping manner. (There’s a saying that concurrency does not imply parallelism.)

Threading is a concurrent execution model whereby multiple threads take turns 
executing tasks. One process can contain multiple threads. 
```bash

                             Concurency
             (tasks have ability to run in overlapping manner)
                   /           \                       \ 
     *--Parralelism---*         \                       \
                /                \                       \
    Multiprocessing(CPU)   *-------Threading(I/O)         \ 
            /                       \                      \
    multiprocessing   concurent.features.Threading     *----asyncio----*
         /                             \                      \
Many processes(many GILs)  preemptive multitasking    cooperative multitaksing
```

- Asynchronous routines are able to “pause” while waiting on their ultimate result and let other routines run in the meantime.

- Asynchronous code, through the mechanism above, facilitates concurrent execution. To put it differently, asynchronous code gives the look and feel of concurrency.

A coroutine is a specialized version of a Python generator function. Let’s start with a baseline definition and then build off of it as you progress here: a coroutine is a function that can suspend its execution before reaching return, and it can indirectly pass control to another coroutine for some time.

```python
async def f(x):
    y = await z(x)  # OK - `await` and `return` allowed in coroutines
    return y

async def g(x):
    yield x  # OK - this is an async generator

async def m(x):
    yield from gen(x)  # No - SyntaxError

def m(x):
    y = await z(x)  # Still no - SyntaxError (no `async def` here)
    return y
```

## Relevant methods

```python
# Runs event loop
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
```