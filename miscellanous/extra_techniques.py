import itertools
from collections import Counter

# Trick 1: Flatten the lists
a = [[1,2], [3,4], [5,6]]
b = list(itertools.chain.from_iterable(a))
print(b)

# Trick 2: Reverse a list
a = ["10", "9", "8", "7"]
print(a[::-1])

# Trick 3: Combining different lists / Transposing a 2D list
a = ["a", "b", "c", "d"]
b = ["e", "f", "g", "h"]
result = [ list(row) for row in list(zip(a,b))]
print(result)

# Trick 4: Negative indexing lists
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[-3:-1])

# Trick 5: Analyzing the most frequent on the list
a = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(a.count(4))
most_freq = max(set(a), key=a.count)
print(most_freq)

words = ["apple", "banana", "cherry", "date", "fig"]
sorted_words = sorted([x+"dupa" for x in words], key=len)
print(sorted_words)
# Output: ['date', 'fig', 'apple', 'cherry', 'banana']

# Trick 6: Reversing the string
a="python"
print("Reverse is", a[::-1])

# Trick 7: Splitting the string
a="python is the language of futher"
b= a.split()
print(b)

# Trick 8: Printing out multiple values of strings
print("on" * 3 + "off" * 2)

# Trick 9: Creating a single string
a = ["i", "am", "not", "a", "joke"]
print("".join(a))

def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)
print(is_anagram('taste', 'staet'))
print(is_anagram('beach', 'peahc'))

# Trick 15: Merging multiple dictionaries
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}
print(z)

# print(list(map(int, input("enter numbers:").split())))

# Maps

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Define a function that squares a number
def square(x):
    return x ** 2

# Use map to apply the square function to each number in the list
squared_numbers = map(square, numbers)
print(squared_numbers)

# Convert the result to a list (in Python 3, map returns a map object)
squared_numbers_list = list(squared_numbers)

print(squared_numbers_list)
# Output: [1, 4, 9, 16, 25]