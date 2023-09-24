from functools import reduce

numbers = [1, 2, 3, 4, 5]

# MAP
squared_numbers = map(lambda x: x**2, numbers)
print(set(squared_numbers))
# {1, 4, 9, 16, 25}

# REDUCE
sum_of_numbers = reduce(lambda x, y: x+y, numbers)
print(sum_of_numbers)
# 15

sum_of_numbers = reduce(lambda x, y: x+y, map(lambda x: x**2, range(1,6)))
print(sum_of_numbers)
# 55 ( maps range to square then add all the numbers)

# FILTER
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))
# <filter object at 0x104847340>
# 2,4

# Conditional Comprehensions
numbers = [1, 2, 3, 4, 5]
squared_even_numbers = [x**2 for x in numbers if x % 2 == 0]

# Generator expressions
numbers = [1, 2, 3, 4, 5]
squared_even_numbers = (x**2 for x in numbers if x % 2 == 0)
print(squared_even_numbers)
# <generator object <genexpr> at 0x104870040>


for number in [x**2 for x in numbers if x % 2 == 0]:
    print(number)
# Lazy evaluation, calculates number on each iteration, 
# in case of lists entire list is calculated into memory first
# 4 16

for number in [x**2 for x in numbers if x % 2 == 0]:
    print(number)

# 4 16 Same result but memory inefficient

# ZIP
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
combined_data = zip(names, ages)
print(list(combined_data))
# <zip object at 0x1009b5580>
# [('Alice', 30), ('Bob', 25), ('Charlie', 35)]


names = ["Alice", "Bob", "Charlie"]
indexed_names = enumerate(names, start=1)
print(indexed_names)
# <enumerate object at 0x102b42a70>
# [(1, 'Alice'), (2, 'Bob'), (3, 'Charlie')]
