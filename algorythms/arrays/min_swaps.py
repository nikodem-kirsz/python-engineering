import unittest

def min_swaps(number): # 7298
    max_number = 0
    max_second_number = 0
    max_number_index = 0
    max_second_number_index = 0

    for index, char in enumerate(str(number)):
        print(int(char))
        num = int(char)
        if num > max_number and num > max_second_number:
            max_second_number = max_number
            max_second_number_index = max_number_index
            max_number = num
            max_number_index = index
        elif num < max_number and num > max_second_number:
            max_second_number = num
            max_second_number_index = index
    
    print(f"max_number: {max_number}, max_number_index: {max_number_index}")
    print(f"max_second_number: {max_second_number}, max_second_number_index: {max_second_number_index}")

    new_number = [int(digit) for digit in str(number)]
    new_number[0], new_number[max_number_index] = new_number[max_number_index], new_number[0]
    new_number[1], new_number[max_second_number_index] = new_number[max_second_number_index], new_number[1]
    
    return int(''.join(map(str, new_number)))


class TestMinSwaps(unittest.TestCase):
    def test_min_swaps(self):
        number = min_swaps(7889)
        self.assertEqual(number, 9887)

if __name__ == "__main__":
    unittest.main()

