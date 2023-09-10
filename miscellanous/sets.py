s = set({1,2,3,4})
print(type(s))
d = set([1,2,3])
print(d)
type(s)

s = {1, 2, 3, 2, 3, 4}

s.add(4)
s.update([2, 3, 4, 5, 6])
s.remove(3)
s.discard(3)
s.remove(2)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2))


s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}
s1.intersection(s2, s3)
print(f'intersection: {s1}')

s1 = {1, 2, 3}
s2 = {2, 3, 4}

print(s1.difference(s2))  # or 's1 - s2'
# {1}

print(s2.difference(s1))

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1.symmetric_difference(s2))