# call by value or call by reference
# call by object or call by object reference

# there are two rules to be considered
# so parameters are passed in is actually a reference to an object
# but the reference is passed by value.

# And there is a difference between mutable and immutable data types.

# mutable objects like lists or dictionaries can be changed within a method
# but if you rebind the reference in the method then the outer reference will stil
# point to the original object and is not changed.

# immutable objects like integers or strings cannot be changed within a method
# but immutable objects contained within a mutable object  can be reassigned within a method



# immutable objects
def foo(x):
    x = 5

var = 10
foo(var)
print(var)




# mutable objects
def foo(a_list):
    a_list.append(4)

my_list = [1,2,3]
foo(my_list)
print(my_list)




# rebind an immutable reference
def foo(a_list):
    # this is more like a local var now???
    a_list = [200,300,400]
    a_list.append(4)
    a_list[0] = -100

my_list = [1,2,3]
foo(my_list)
print(my_list)
