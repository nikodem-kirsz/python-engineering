import os
import time
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()
            # time.sleep(1)



def my_generator(start, end):
    for i in range(start, end):
        yield i

# Usage


if __name__ == "__main__":
    for line in read_large_file("file.txt"):
        print(line)

    gen = my_generator(1, 5)
    for num in gen:
        print(num)    

