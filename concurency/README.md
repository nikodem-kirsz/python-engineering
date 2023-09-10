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
                         /
     *---------------Parralelism------------------------------*
                /                \                       \
    Multiprocessing(CPU)   *-------Threading(I/O)         \ 
            /                       \                      \
    multiprocessing   concurent.features.Threading     *----asyncio----*
         /                             \                      \
Many processes(many GILs)  preemptive multitasking    cooperative multitaksing
```
