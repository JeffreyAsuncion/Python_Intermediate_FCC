# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
# https://towardsdatascience.com/heres-the-most-efficient-way-to-iterate-through-your-pandas-dataframe-4dad88ac92ee
# this is what trevor explained to me for the saleforce API


# Cartesian Product
from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b)
print(prod)
print(list(prod))

# Cartesian Product withrepeat = 2
from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b, repeat=2)
print(prod)
print(list(prod))


# to calculate the permentations
from itertools import permutations
a = [1, 2, 3]
perm = permutations(a)
print(perm)
print(list(perm))


# change length =2 , to calculate the permentations
from itertools import permutations
a = [1, 2, 3]
perm = permutations(a, 2)
print(perm)
print(list(perm))


# combination, length in mandatory, let's set it to 2
from itertools import combinations
a = [1,2,3,4]
comb = combinations(a, 2)
print(comb)
print(list(comb))


# combination with replacemet allows for duplicate
# , length in mandatory, let's set it to 2
from itertools import combinations, combinations_with_replacement
a = [1,2,3,4]
comb = combinations(a, 2)
print(comb)
print(list(comb))
comb_wr = combinations_with_replacement(a, 2)
print(comb_wr)
print(list(comb_wr))


# Accumulate, default is to compute the sums
from itertools import accumulate
a = [1,2,3,4]
acc = accumulate(a)
print(a)
print(acc)
print(list(acc))


# Accumulate, we can multiple the elements
from itertools import accumulate
import operator
a = [1,2,3,4]
acc = accumulate(a, func=operator.mul)
print(a)
print(acc)
print(list(acc))


# Accumulate, we can find max of the elements
from itertools import accumulate
import operator
a = [1,2,5,3,4]
acc = accumulate(a, func=max)
print(a)
print(acc)
print(list(acc))



# groupby, we can use a key = function
from itertools import groupby
def smaller_than_3(x):
    return x < 3

a = [1,2,3,4, 5]
group_obj = groupby(a, key=smaller_than_3)
print(group_obj)
for key, value in group_obj:
    print(key, list(value))



# groupby, we can use a lambda == same as above
from itertools import groupby

a = [1,2,3,4, 5]
group_obj = groupby(a, key=lambda x: x<3)
print(group_obj)
for key, value in group_obj:
    print(key, list(value))




# groupby, we can use a lambda == same as above
from itertools import groupby

persons=[
    {'name': 'Tim', 'age': 25},
    {'name': 'Dan', 'age': 25},
    {'name': 'Lisa', 'age': 27},
    {'name': 'Claire', 'age': 28}
]

group_obj = groupby(persons, key=lambda x: x['age'])
print(group_obj)
for key, value in group_obj:
    print(key, list(value))



# infinite loop with count
from itertools import count

# this will make an infinite loop that starts at 10
for i in count(10):
    print(i)
    # this will continue as an infinite loop
    if i == 15:
        break



# infinite loop with count
from itertools import cycle, repeat

# this will make an infinite loop that starts at 10
a = [1,2,3]
count = 0
for i in cycle(a):
    print(i)
    # if not will continue infinitely
    if count == 10:
        break
    count += 1



# infinite loop with repeat
from itertools import repeat

# this will make an infinite loop that starts at 10
a = [1,2,3]
# the 4 is the number of repetitions
for i in repeat(1, 4):
    print(i)

 



