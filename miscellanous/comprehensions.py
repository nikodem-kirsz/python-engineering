# List Comprehensions are a special kind of syntax that let us create lists out of other lists, 
# and are incredibly useful when dealing with numbers and with one or two levels of nested for loops.

names = ['Charles', 'Susan', 'Patrick', 'George']

new_list = []

for name in names:
    new_list.append(name)
    new_list.remove(name)

print(new_list)

new_list = [n for n in names]

print(new_list)

n = [(a, b) for a in range(1,3) for b in range(1,3)]
print(n)

new_list = [n for n in names if n.startswith('C')]
print(new_list)

nums = [1,2,3,4,5,6]
new_list = [lambda num: num*2 if num % 2 == 0 else num*1000 for _ in nums]
print(len(new_list))
for func, i in zip(new_list, range(1,len(new_list))):
    print(func(i))

# Set comprehension
b = {"abc", "def"}
{s.upper() for s in b}
# {'ABC', 'DEF'}

# Dictionary comprehension e.g switching key and values
c = {'name': 'Pooka', 'age': 5}
{v: k for k, v in c.items()}
# {'Pooka': 'name', 5: 'age'}

c = {'name': 'Pooka', 'age': 5}
["{}:{}".format(k.upper(), v) for k, v in c.items()]
# ['NAME:Pooka', 'AGE:5']