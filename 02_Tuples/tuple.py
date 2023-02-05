# Tuples: ordered, immutable, allow duplicate elements
# can not be changed after creation
mytuple = ("Max", 28, "Boston")
print(mytuple)

# parenthesis are optional but comma is mandatory
mytuple = "Max", 28, "Boston"
print(mytuple)

# one element tuple, notice type is string not tuple 
# see next example
mytuple = ("Max")
print(type(mytuple))


# one element tuple, notice the comma definites it a tuple 
# note the comma and the type
mytuple = ("Max",)
print(type(mytuple))

# create a tuple from a list
mytuple = tuple(["Max", 28, "Boston"])
print(mytuple)


# get element from tuple using Index
item = mytuple[0]
print(item)

# negative Index
item = mytuple[-1]
print(item)


# if Index is too large
# item = mytuple[5]
# print(item)
# IndexError: tuple index out of range

# what happens if we try to change an element of a tuple
# chnage using index and assignment
# mytuple[0] = "Tim"
# Type Error: 'tuple' object does not support item assignment


# iterate thru a tuple
for i in mytuple:
    print(i)


# check if element is "in" the tuplel
if "Max" in mytuple:
    print("here")
else:
    print("not here")


my_tuple = ['a','p','p','l','e']
print(len(my_tuple))


# count a certain element in a tuple
print(my_tuple.count('p'))


# find the first index of an element
print(my_tuple.index('p'))


# convert tuple to list
my_list = list(my_tuple)
print(my_list)


# convert list to tuple
my_tuple2 = tuple(my_list)
print(my_tuple2)


# slicing with tuples, all slicing like list apple here
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5]
print(b)



# tuple unpacking
my_tuple = "Max", 28, "Boston"
name, age, location = my_tuple
print(name)
print(age)
print(location)


# advanced tuple unpacking
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
i1, *i2, i3 = my_tuple
print(i1)
print(i2)
print(i3)


# when working with large data a tuple is more efficient
import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")


import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))