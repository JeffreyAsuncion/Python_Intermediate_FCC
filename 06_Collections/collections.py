# collections: Counter, namedtuple, OrderedDict, defaultdict, dequeue

from collections import Counter

# Counter is a container 
# that stores the elements as dictionary keys
# their counts as dictionary values

a = "aaaaaabbbbbcccc"
my_counter = Counter(a)
print(my_counter)
# .keys(), .values(), .items()
print(my_counter.most_common(1))
# 1 == just the first most common (returns tuple)
# 2 == just the first and second most common (returns tuple)

print(list(my_counter.elements()))



# namedtuple is like a struct

from collections import namedtuple

Point = namedtuple('Point', 'x,y')
pt = Point(1,-4)
print(pt.x, pt.y)



# OrderedDict
# like an ordinary dictionary but remembers the order of the keys
# dicts in Python 3.7 and higher have this functionality built-in

from collections import OrderedDict

ordered_dict = OrderedDict()

ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5
ordered_dict['f'] = 6
ordered_dict['g'] = 7

print(ordered_dict)



# defaultdict
# same as ordinary dict but if key has no value then value will be a default value

from collections import defaultdict

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['c']) # if this was a ordinary dict, this would throw a KeyError
# note default set to 0 for int




# deque

from collections import deque

d = deque()


d.append(1)
d.append(2)

d.appendleft(3)

print(d)

d.extendleft([4,5,6])
print(d)

d.rotate(1)# rotate one to the right
print(d)

