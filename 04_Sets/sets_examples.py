# Sets: unordered, mutable, no duplicates

myset = {1,2,3,1}
print(myset)

myset = set("hello")
print(myset)

# note this is a dictionary, not a set
myset = {}
print(type(myset))

myset = set()
print(type(myset))


myset = set()

myset.add(1)
myset.add(2)
myset.add(3)
myset.add(4)
myset.remove(3) # not present will KeyError
myset.discard(3) # will not KeyError
# myset.clear()
print(myset.pop())
print(myset)


for i in myset:
    print(i)

if 2 in myset:
    print('yes')



# Union and Intersection
odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8}
primes = {2, 3, 5, 7}

unionSet = odds.union(evens)
print(unionSet)

intersectionSet = odds.intersection(evens)
print(intersectionSet)

intersectionSetOddsPrimes = odds.intersection(primes)
print(intersectionSetOddsPrimes)

intersectionSetEvensPrimes = evens.intersection(primes)
print(intersectionSetEvensPrimes)


set_A = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_B = {1, 2, 3, 10, 11, 12}
difference = set_A.difference(set_B)
print(difference)
difference = set_A.symmetric_difference(set_B)
print(difference)

# to update or fill
set_A.update(set_B)
print(set_A)

# to update just the intersection
set_A = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_B = {1, 2, 3, 10, 11, 12}
set_A.intersection_update(set_B)
print(set_A)


# to update just the difference
set_A = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_B = {1, 2, 3, 10, 11, 12}
set_A.difference_update(set_B)
print(set_A)


# to update just the difference
set_A = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_B = {1, 2, 3, 10, 11, 12}
set_A.symmetric_difference_update(set_B)
print(set_A)





set_A = {1, 2, 3, 4, 5, 6}
set_B = {1, 2, 3}
set_C = {7, 8}

print(set_A.issubset(set_B))
print(set_B.issubset(set_A))

print(set_A.issuperset(set_B))
print(set_B.issuperset(set_A))

print(set_A.isdisjoint(set_B))
print(set_B.isdisjoint(set_C))


# copying sets
set_A = {1, 2, 3, 4, 5, 6}
set_B = set_A.copy()
# set_B = set(set_A)
set_B.add(7)
print(set_B)
print(set_A)



# frozenset
# this is just an immutable version of a normal set
a = frozenset([1,2,3,4])
b = frozenset([3,7,8])
## these don't work
# a.add(1)
# a.remove(1)

# but Union, Intersection and Difference will work
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))