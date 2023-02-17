"""
- The difference between arguments and parameters
- Positional and keyword arguments
- Default arguments
- Variable-length arguments (*args and **kwargs)
- Container unpacking into function arguments
- Local vs. global arguments
- Parameter passing (by value or by reference?)
"""

# name is our parameter
def print_name(name):
    print(name)

# 'Alex' is our argument
print_name('Alex')



def foo(a,b,c):
    print(a,b,c)

# positional arguments
foo(1,2,3)
# keyword arguments (order doesn't matter)
foo(a=1, b=2, c=3)
# position (1st) and keyword (2nd)
foo(1, b=2, c=3)
# position (1st) and keyword (2nd) and positional (3rd)
# SyntaxError: positional argument follows keyword
# foo(1, b=2, 3)


# d has a default value in the function definition
def foo_withDefault(a,b,c, d=4):
    print(a,b,c,d) 
#d does not need to be passed it is passed by default
foo_withDefault(1,2,3)
# i can override the default by assigning in the function call
foo_withDefault(1,2,3,4)



# variable length arguments
# * == any number of positional arguments
# ** == any number of keyword arguments
def foo(a, b, *args, **kwargs):
    print(a,b)
    # args is a tuple
    for arg in args:
        print(arg)
    # kwargs is a dictionary
    for key in kwargs:
        print(key,kwargs)

foo(1,2,3,4,5, six=6,seven=7)
    



# force keyword arguments using just a *
def foo(a, b, *, c, d):
    print(a, b, c, d)
# this forces the use, after the *, must be a keyword argument
foo(1, 2, c=3, d=4)


# force keyword arguments using just a *
def foo(*args, last):
    for arg in args:
        print(arg)
    print("last",last)
# this forces the use, after the *, must be a keyword argument
foo(1, 2, 3, last=4)




# unpacking arguments using the prefix * to unpack
# the num_of_parameters must match the unpacked num
def foo(a,b,c):
    print(a,b,c)

mylist = [0, 1, 2]
foo(*mylist)



# unpacking arguments using the prefix * to unpack
# the num_of_parameters must match the unpacked num
def foo(a,b,c):
    print(a,b,c)

mydict = {'a':0, 'b':1, 'c':2}
foo(**mydict)








