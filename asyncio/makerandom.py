"""
This program uses one main coroutine, makerandom(), and runs it concurrently 
across 3 different inputs. Most programs will contain small, modular 
coroutines and one wrapper function that serves to chain each of the smaller 
coroutines together. main() is then used to gather tasks (futures) by mapping
the central coroutine across some iterable or pool.
"""
import asyncio
import random

c = (
    "\033[0m",
    "\033[36m",
    "\033[91m",
    "\033[35m",
)

async def makerandom(idx: int, threshold: int = 6) -> int:
    ...
    print(c[idx + 1] + f"Initiated makerandom({idx}),")
    i = random.randint(0, 10)
    while(i <= threshold):
        print(c[idx + 1] + f"makerandom({idx}) == {i} too low; retrying.")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(c[idx + 1] + f"----> Finished: makerandom({idx}) == {i}" + c[0])
    return i    

async def main():
    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
    return res

if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")