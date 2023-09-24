import sys

# Check the memory size of an integer
integer_value = 255_255_255_255_255_255_255_255
memory_size = sys.getsizeof(integer_value)
print(f"Memory size of integer: {memory_size} bytes")

# Check the memory size of a floating-point number
float_value = 42.0
memory_size = sys.getsizeof(float_value)
print(f"Memory size of float: {memory_size} bytes")

# Check the memory size of a complex number
complex_value = 2 + 3j
memory_size = sys.getsizeof(complex_value)
print(f"Memory size of complex: {memory_size} bytes")

# Check the memory size of an long integer
long_value = 9999999999999999999999999999
memory_size = sys.getsizeof(long_value)
print(f"Memory size of long: {memory_size} bytes")
