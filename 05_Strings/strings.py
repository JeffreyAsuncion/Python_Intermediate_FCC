# Strings: ordered, immutable, text representation

my_string = 'Hello World!'
print(my_string)

char = my_string[-1]
print(char)

substring = my_string[1:5]
print(substring)

revstring = my_string[::-1]
print(revstring)

for i in my_string:
    print(i)

if 'e' in my_string:
    print('yes')

my_string = '            Hello World    '
my_string = my_string.strip()
print(my_string)


my_string = "Hello World!"
print(my_string.endswith('!'))

print(my_string.find('o'))
print(my_string.count('l'))
print(my_string.replace('World','Universe'))

my_string = "how are you doing"
my_list = my_string.split()
print(my_list)

new_string = ' '.join(my_list)
print(new_string)


my_list = ['a'] * 10
print(my_list)

from timeit import default_timer as timer

# bad Python code
start = timer()
my_string = ''
for i in my_list:
    # this operation is expensive, creating another string each iteration
    my_string += i
stop = timer()
print(my_string, stop-start)

# good Python code
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(my_string, stop-start)



# format strings,  %, .format(), f-Strings

var = 'Tom'
my_string = "the variable is %s" % var
print(my_string)


var = 3.13463764
my_string = "the variable is %.2f" % var
print(my_string)



var = 3.13463764
my_string = "the variable is {:.2f}".format(var)
print(my_string)


var = 3.13463764
my_string = f"the variable is {var:.2f}"
print(my_string)