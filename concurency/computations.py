import multiprocessing
import time
import queue

POW = 300
N = 1000000
def function_1(n, result_queue):
    sum_val = 0
    for i in range(n):
        sum_val += (i + 100000) ** POW
    result_queue.put(sum_val)

def function_2(n, result_queue):
    sum_val = 0
    for i in range(n):
        sum_val += (i + 100000) ** POW
    result_queue.put(sum_val)

def function_3(n, result_queue):
    sum_val = 0
    for i in range(n):
        sum_val += (i + 100000) ** POW
    result_queue.put(sum_val)

if __name__ == "__main__":
    # Create a multiprocessing.Queue to collect results
    result_queue = multiprocessing.Queue()


    # Create Process objects for each function and pass arguments as tuples
    process_1 = multiprocessing.Process(target=function_1, args=(N, result_queue))
    process_2 = multiprocessing.Process(target=function_2, args=(N, result_queue))
    process_3 = multiprocessing.Process(target=function_3, args=(N, result_queue))

    start = time.time()
    # Start each process
    process_1.start()
    process_2.start()
    process_3.start()

    # Optionally, wait for all processes to complete
    process_1.join()
    process_2.join()
    process_3.join()
    

    # Collect and print the results from the queue
    results = []
    for _ in range(3):
        result = result_queue.get()
        results.append(result)

    print("All processes have completed")
    print("Results:", results)

    print(f"Duration: {time.time() - start:0.2f} seconds")
    # Duration: 9.15 seconds

    print("-" * 10 + "Single processor" + "-" * 10)
    start = time.time()
    qu = queue.Queue()
    function_1(N, qu)
    function_2(N, qu)
    function_3(N, qu)

    results = []
    for _ in range(3):
        result = qu.get()
        print(result)
        results.append(result)


    print("All processes have completed")
    print("Results:", results)

    print(f"Duration: {time.time() - start:0.2f} seconds") 
    # Duration: 25.72 seconds  
