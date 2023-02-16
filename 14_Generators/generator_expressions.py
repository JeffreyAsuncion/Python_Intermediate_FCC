import sys

mygenerator = (i for i in range(1000000) if i % 2 == 0)
print(sys.getsizeof(mygenerator))

# for i in mygenerator:
#     print(i)

mylist = [ i for i in range(1000000) if i % 2 == 0]
print(sys.getsizeof(mylist))

# for i in mylist:
#     print(i)