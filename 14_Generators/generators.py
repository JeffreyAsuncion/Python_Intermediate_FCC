# Generators return an object that can be iterated over
# they generate items inside the object lazily, 
# which means they generatethe items only one at a time
# and only when you ask for it. 
# much more memory efficient than other sequence object 
# when you have to deal with large datasets.

# defined like a normal funciton 
# but with yield keyword instead of return keyword

def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()

## you can iterate thru generator
# for i in g:
#     print(i)

## you can use next to iterate one by one (per each yield statement)
value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)

## this will cause 
## StopIteration Error
# value = next(g)
# print(value)
