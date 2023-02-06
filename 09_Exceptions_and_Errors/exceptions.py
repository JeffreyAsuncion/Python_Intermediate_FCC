# Error and Exceptions

# Difference between a syntax error and an exception
# what are the most common built-in exceptions
# how do we raise and handle exceptions
# how do we define our own exceptions

# Syntax Error
# a syntax error occurs went the parser detects
# an incorrect statemnet 


# a = 5 print(a) # SyntaxError: invalid syntax


# a = 5
# print(a)) # SyntaxError: unmatched ')


# a = 5 +'10' # TypeError


# import somemodule # ModuleNotFoundError: No module named 'somemodule'


# a = 5
# b = c # NameError: name 'c' is not defined


# f = open('somefile.txt')    # FileNotFoundError


# a = [1, 2, 3]
# a.remove(4) # ValueError
# print(a)


# a = [1, 2, 3]
# a[4]    # IndexError
# print(a)


# my_dict = {"name": "Max"}
# my_dict['age']  # KeyError


# x = -5
# if x < 0:
#     raise Exception('x should be positive')   # raises an Exception


# x = -5
# assert (x>=0), 'x is not positive'  #raises an AssertionError


# Exception Handling
try:
    a = 5/0     # program does not stop, it continues and a except is flagged
except:
    print('an error happened')


# catch the type of Expection
try:
    a = 5/0     # program does not stop, it continues and a except is flagged
except Exception as e:
    print(e)


# catch the ZeroDivisionError
try:
    a = 5 / 1
    b = a + '10'     
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    # this fires if no excpetions
    print('everything is fine. No exceptions occurred!')



# else clause will fire if no exceptions occur
try:
    a = 5 / 1
    b = a + 5     
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    # this fires if no excpetions
    print('everything is fine. No exceptions occurred!')



# finally clause will always fire 
# finally is usually for cleanup operations
try:
    a = 5 / 1
    b = a + 5     
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    # this fires if no excpetions
    print('everything is fine. No exceptions occurred!')
finally:
    # usually for clean up operations
    print("cleaning up!!!")




# how to define our own excpections
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('value is too small', x)

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)





