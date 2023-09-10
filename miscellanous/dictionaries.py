import pprint

my_cat = {
    'size': 'fat',
    'color': 'gray',
    'disposition': 'loud'
}

my_cat['age_years'] = 2
print(my_cat)

print(my_cat['size'])


pet = {'color': 'red', 'age': 42}
for value in pet.values():
    print(value)

for key in pet.keys():
    print(key)

for item in pet.items():
    print(f'key: {item[0]}, value: {item[1]}')

for key, value in pet.items():
    print(f'Key: {key} Value: {value}')

wife = {'name': 'Rose', 'age': 33}

f'My wife name is {wife.get("name")}'
f'She is deeply in love with {wife.get("husband", "lover")}'
wife.setdefault('has_hair', True)

wife.pop('age')
wife.popitem()
# del wife['age']
wife.clear()
person = {'name': 'Rose', 'age': 33}
'name' in person.keys()
'height' in person.keys()


wife = {'name': 'Rose', 'age': 33, 'has_hair': True, 'hair_color': 'brown', 'height': 1.6, 'eye_color': 'brown'}
pprint.pprint(wife)

dict_a = {'a': 1, 'b': 2}
dict_b = {'b': 3, 'c': 4}
print({**dict_b})
dict_c = {**dict_a, **dict_b}
print(f'dict_c: {dict_c}')