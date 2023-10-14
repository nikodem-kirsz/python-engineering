import unittest

def merge_sort(arr):
    if len(arr) <= 1:
        return arr # [1]
    
    mid = len(arr) // 2
    print(mid)

    left_half, right_half = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    print('LEFT_HALF', left_half)
    print('RIGHT_HALF', right_half)

    return merge(left_half, right_half)
    

def merge(left_arr, right_arr): # [1,2,3] [4,5,7]
    result = []
    left_index, right_index = 0, 0

    print('insidde merge')

    while left_index < len(left_arr) and right_index < len(right_arr):
        print(left_index, right_index)
        if left_arr[left_index] < right_arr[right_index]:
            result.append(left_arr[left_index])
            left_index += 1
        else:
            result.append(right_arr[right_index])
            right_index += 1

    return result + left_arr[left_index:] + right_arr[right_index:]

class TestMergeSort(unittest.TestCase):
    def dtest_merge_sort(self):
        arr = [1,3,2,5,4,7]
        sorted_list = merge_sort(arr)
        self.assertEqual(sorted_list, [1,2,3,4,5,7])
    def test_merge(self):
        arr1 = [1,3,7]
        arr2 = [2,4,5]

        merged = merge(arr1, arr2)
        self.assertEqual(merged, [1,2,3,4,5,7])

if __name__ == "__main__":
    unittest.main()