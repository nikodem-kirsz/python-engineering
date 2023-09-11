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
asyncio.run()
asyncio.new_event_loop()
asyncio.gather(future(), future(), past(), future())
asyncio.create_task(coro([3,2,1]))
asyncio.all_tasks()
asyncio.sleep(1)


routine = main()
asyncio.run(routine)
loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close() 


t1 = asyncio.create_task(coro([3,2,1]))
t2 = asyncio.create_task(coro([10,5,0]))
for res in asyncio.as_completed((t1, t2)):
    compl = await res   
```