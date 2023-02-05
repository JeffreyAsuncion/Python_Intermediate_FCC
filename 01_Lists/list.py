# Lists: ordered, mutable, allows duplicate elements
mylist = ["banana", "cherry", "apple"]
print(mylist)

# create an empty list with a list() function
mylist2 = list()
print(mylist2)

# List allow for different data types 
mylist2 = [5, True, "apple"]
print(mylist2)

# List allow for duplicate elements 
mylist2 = [5, True, "apple", "apple"]
print(mylist2)

# access an element by using the index
item = mylist[0]
print(item)

# if index is too large
# IndexError: list index out of range
# item = mylist[3]

# index can be negative -1 == the last item in the list
item = mylist[-1]
print(item)

# if you want to iterate over your list
for i in mylist:
    print(i)

# to check if an item is in a list
if "banana" in mylist:
    print("yes")
else:
    print("no")

# to check if an item is in a list
if "lemon" in mylist:
    print("yes")
else:
    print("no")

# to check how many elements in your list
print(len(mylist))


# to append items
mylist.append("lemon")
print(mylist)

# to insert at a certain position
mylist.insert(1, "blueberry")
print(mylist)

# to remove items
item =  mylist.pop()
print(item, mylist)

# to remove items with pop()
item = mylist.remove("cherry")
print(mylist)

# to remove items with pop()
# if item not in list
# # ValueError: list.remove(x)
# item = mylist.remove("cherry1")
# print(mylist)

# remove all elements
# mylist.clear()
# print(mylist)

# to reverse the list, reverse method
mylist.reverse()
print(mylist)

# sort list, sorts the list in-place
mylist.sort()
print(mylist)

# sort list with numbers, sorts the list in-place
mylist = [4, 3, 1, -1, -5, 10]
mylist.sort()
print(mylist)

# sort list with numbers, with sorted not in-place
# original list is not sorted
mylist = [4, 3, 1, -1, -5, 10]
new_list = sorted(mylist)
print(mylist)
print(new_list)


# create a new list with the same elements
mylist = [0] * 5
print(mylist)

# concate two list with the + operator
mylist2 = [1,2,3,4,5]
new_list = mylist + mylist2
print(new_list)


# slicing [(starting) : (upto and excluding)]
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[1:5]
print(a)

# reverse a list with slicing
print(mylist[::-1])




# copying a list
list_original = ["banana", "cherry", "apple"]
# copy but be careful, points to same list in memory
list_copy = list_original

#if i modify the copy, i modify the original
list_copy.append("lemon")

print(list_copy)
print(list_original)




# copying a list
list_original = ["banana", "cherry", "apple"]
# I use the copy method, to make a copy
list_copy = list_original.copy()
# list_copy = list(list_original)
# list_copy = list_original[:]


#if i modify the copy, i modify the original
list_copy.append("lemon")

print(list_copy)
print(list_original)


# list comprehension
mylist = [1, 2, 3, 4, 5, 6] 
b = [i*i for  i in mylist]
# this is the same as 
# a = []
# for i in mylist:
#     a.append(i*i)
print(mylist, b)


