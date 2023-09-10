import concurrent.futures
import time
import multiprocessing

def merge_sort(arr): # [1,2,3,4,5,6,7,8]
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    leftArr = arr[:mid] # [1,2,3,4]
    rightArr = arr[mid:] # [5,6,7,8]

    leftArr = merge_sort(leftArr)
    rightArr = merge_sort(rightArr)

    return merge(leftArr, rightArr)

def merge(arr1, arr2): # [1,2] [3,4]
    leftIndex, rightIndex = 0, 0
    result = []

    while leftIndex < len(arr1) and rightIndex < len(arr2):
        if arr1[leftIndex] > arr2[rightIndex]:
            result.append(arr1[leftIndex])
            leftIndex += 1
        else:
            result.append(arr2[rightIndex])
            rightIndex += 1

    result.extend(arr1[leftIndex:])
    result.extend(arr2[rightIndex:])      
    return result

def merge_sort_parrelel(arr): # [1,2,3,4,5,6,7,8]
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    leftArr = arr[:mid] # [1,2,3,4]
    rightArr = arr[mid:] # [5,6,7,8]

    # with concurrent.futures.ThreadPoolExecutor() as executor:
    with multiprocessing.Pool() as pool:
        # left_future = executor.submit(merge_sort, leftArr)
        # right_future = executor.submit(merge_sort, rightArr)
        leftArr = pool.apply(merge_sort, (leftArr,))
        rightArr = pool.apply(merge_sort, (rightArr,))

        # leftArr = left_future.result()
        # rightArr = right_future.result()

    return merge(leftArr, rightArr)

if __name__ == '__main__':
    print(merge_sort([1,2,5,4,22,7, 22]))

    start_time = time.time()
    print(merge_sort([num for num in range(1,10000000)]))
    end_time = time.time()
    execution_time = end_time - start_time
    print(f'Execution time: {execution_time:.6f} seconds')