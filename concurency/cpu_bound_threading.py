import time
import multiprocessing

# single core cpu version of processing - suming 1..long_int of square long int numbers in 20 element list
# [
# 5000000, 5000001, 5000002, 5000003, 5000004, 5000005, 5000006, 5000007, 5000008, 5000009, 5000010, 
# 5000011, 5000012, 5000013, 5000014, 5000015, 5000016, 5000017, 5000018, 5000019
# ]

# [
# 41666654166667500000, 41666679166667500000, 41666704166677500001, 41666729166697500005, 41666754166727500014, 
# 41666779166767500030, 41666804166817500055, 41666829166877500091, 41666854166947500140, 41666879167027500204, 
# 41666904167117500285, 41666929167217500385, 41666954167327500506, 41666979167447500650, 41667004167577500819, 
# 41667029167717501015, 41667054167867501240, 41667079168027501496, 41667104168197501785, 41667129168377502109
# ]

# one core version took 4,04s
# 8 core(default cpu) concurent computing version took 0.91s


def cpu_bound(number):
    print(multiprocessing.Process())
    return sum(i * i for i in range(number))

def find_sums(numbers):
    result = [] 
    with multiprocessing.Pool() as pool:
        result = pool.map(cpu_bound, numbers)
    return result

if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]
    print(numbers)

    start_time = time.time()
    print(find_sums(numbers))
    duration = time.time() - start_time

    print(f'Duration {duration} seconds')

