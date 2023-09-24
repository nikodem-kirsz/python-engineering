students = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 22},
    {'name': 'Charlie', 'age': 30}
]

# Sort the list of dictionaries by 'age' key
sorted_students = sorted(students, key=lambda x: x['age'])

employee_data = [
    ('Alice', 'HR', 50000),
    ('Bob', 'IT', 60000),
    ('Charlie', 'HR', 55000),
    ('David', 'IT', 62000)
]

# Sort employees by department and then by salary
sorted_employees = sorted(employee_data, key=lambda x: (x[1], x[2]))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person('Alice', 25), Person('Bob', 22), Person('Charlie', 30)]

# Sort a list of custom objects by the 'age' attribute
sorted_people = sorted(people, key=lambda x: x.age)

words = ['apple', 'Banana', 'cherry', 'date', 'apricot']

# Sort a list of strings case-insensitively
sorted_words = sorted(words, key=lambda x: x.lower())

def custom_sort_key(word):
    return (len(word), word)

words = ['apple', 'banana', 'cherry', 'date', 'apricot']

# Sort words by length and then lexicographically
sorted_custom = sorted(words, key=custom_sort_key)
print(sorted_custom)