from collections import Counter

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
count = Counter(data)
print(count)
# Counter({4: 4, 3: 3, 2: 2, 1: 1})

from collections import defaultdict

fruit_counts = defaultdict(int)
fruit_counts['apple'] += 1  # No KeyError

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)
# Point(x=1, y=2)

from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(f'Queue: {queue}')
# Queue: deque([1, 2])
item = queue.popleft()
print(f'Popping left {item}')
# Popping left 1
item = queue.pop()
print(f'Popping right {item}')
# Popping right 2
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['a'] = 1
print(ordered_dict)
# OrderedDict([('b', 2), ('a', 1)])

from collections import ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
combined = ChainMap(dict1, dict2)
print(combined)
# ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})

values = [True, False, True]
any_true = any(values)  # True
all_true = all(values)  # False
