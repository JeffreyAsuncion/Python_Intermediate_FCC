# uses of the asterisk or star sign in Python

# - multiplication
# - power operations
# - creation of lists or tuples with repeated elements
# - args, kwargs
# - keyword onlye parameters
# - unpacking lists, tuples, dictionaries into function arguments
# - unpacking containers
# - merging container into a  list
# - merging two dictionaries


# multiplication
result = 5 * 7
print(result)

# power operation
result = 2 ** 16
print(result)

# create a strings, list, tuple, dictionaries with repeated elements
zeros = [0] * 10
print(zeros)
zeros = [0, 1] * 10
print(zeros)
zeros = (0, 1) * 10
print(zeros)
zeros = "AB" * 10
print(zeros)



# args, kwargs, and keyword only arguments
# see previous chapter 18
numbers = [1,2,3,4,5,6,7,8,9,0]
*beginning, last = numbers
print(beginning)
print(last)



# merged lists, and tuples
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
new_list = [*my_tuple, *my_list]
print(new_list)




#merge tuple, set
my_tuple = (1, 2, 3)
my_set = {4, 5, 6}
new_list = [*my_tuple, *my_set]
print(new_list)


# merge two dictionaries
dict_a = {'a':1, 'b':2}
dict_b = {'c':3, 'd':4}
my_dict = {**dict_a, **dict_b}
print(my_dict)