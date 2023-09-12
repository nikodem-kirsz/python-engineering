import time
import multiprocessing

def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def fibonacci_recursive(n):
    if n < 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_sequence_recursive(n):
    return fibonacci_recursive(n)

def fibonacci_sequence_recursive_memo(n, memo = {}):
    if n < 2:
        return 1
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci_sequence_recursive_memo(n - 1) + fibonacci_sequence_recursive_memo(n - 2)
        return memo[n]

FIBONACCI_N_GENERATORS = 20000
FIBONACCI_N_RECURSION = 20
FIBONACCI_N_RECURSION_MEMO = 950

def main():
    print(10 * "-" + "CALCULATING FIBONACII WITH GENERATORS" + "-" * 10)
    start = time.time()
    fib_number = None
    for num in fibonacci_sequence(FIBONACCI_N_GENERATORS):
        fib_number = num
    print(f"Fibonacii number for {FIBONACCI_N_GENERATORS}: {fib_number}")
    print(f"Duration of generator fibonacii: {time.time() - start:0.2f} seconds") 
    print(20 * "-")    

    print(10 * "-" + "CALCULATING FIBONACII WITH RECURSION NON MEMOIZED" + "-" * 10)
    start = time.time()
    fib_number = fibonacci_sequence_recursive(FIBONACCI_N_RECURSION)
    print(f"FIBONACCI NUMBER: {fib_number}")
    print(f"N={FIBONACCI_N_RECURSION}, Duration of recursive fibonacii without memoization: {time.time() - start:0.2f}")  
    print(20 * "-") 

    print(10 * "-" + "CALCULATING FIBONACII WITH RECURSION MEMOIZED" + "-" * 10)
    start = time.time()
    fib_number = fibonacci_sequence_recursive_memo(FIBONACCI_N_RECURSION_MEMO)
    print(f"FIBONACCI NUMBER: {fib_number}")
    print(f"N={FIBONACCI_N_RECURSION_MEMO} Duration of recursive fibonacii with memoization: {time.time() - start:0.2f}")  
    print(20 * "-") 

if __name__ == "__main__":
    main()
