import asyncio
import random
import time

"""
Depending on amount of arguments(n) passed to a program, it runs 
n coroutines chain()
1. Each runs part1 so we have n coroutines running part1
2. Because part2 expect p1 to be complete part2 awaits results from part1
3. part1 completes after randed amount of time(up to 10) and prints & returns results
4. part2 coroutines start working sleeping for also randed amount of time
5. part2 reads result from part1, prints and returns it
6. because all awaits in chain are complete coroutine proceeds and ends execution
7. chain coroutine prints chained result
8. another part2 coroutine reads back message received from part1 and performs returns and so..
9 .another part2 coroutine reads back message received from part1 and performs returns and so..
"""

async def part1(n: int) -> str:
    i = random.randint(0, 10)
    print(f"part1({n}) sleeping for {i} seconds")
    await asyncio.sleep(i)
    result = f"result{n}-1"
    print(f"Returning part1({n}) === {result}.")
    return result

async def part2(n: int, arg: str) -> str:
    i = random.randint(0, 10)
    print(f"part2{n, arg} sleeping for {i} seconds")
    await asyncio.sleep(i)
    result = f"result{n}-2 derived from {arg}"
    print(f"Returning part2{n, arg} == {result}.")
    return result
# wrapping coroutine
async def chain(n: int) -> None:
    start = time.perf_counter()
    p1 = await part1(n)
    # switch execution back to event loop
    # only when await returns code proceeds next to second await
    p2 = await part2(n, p1)
    # switch execution back to event loop
    end = time.perf_counter() - start
    print(f"-->Chained result{n} => {p2} (took {end:0.2f}) seconds.")

async def main(*args):
    # function running in event loop
    # creating coroutines pool
    await asyncio.gather(*(chain(n) for n in args))

if __name__ == "__main__":
    import sys
    random.seed(444)
    args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
    start = time.perf_counter()
    # Run event loop
    asyncio.run(main(*args))
    end = time.perf_counter() - start
    print(f"Program finished in {end:0.2f} seconds.")