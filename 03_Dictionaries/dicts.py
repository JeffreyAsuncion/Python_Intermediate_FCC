# Dictionary: Key-Value pairs, Unordered, Mutable

mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

value = mydict["name"]
print(value)

# will raise an error
# value = mydict["lastname"]
# print(value)

# to delete
# del mydict["city"]
# mydict.pop("age")
# mydict.popitem()

# check if key in dictionary
if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["lastname"])
except:
    print("Error")


# iterate thru dict

for key in mydict.keys():
    print(key)

for value in mydict.values():
    print(value)

for key,value in mydict.items():
    print(key, value)


# copy dictionary, note dictionary are mutable to make an independent copy use deepcopy
mydict_cpy = mydict.copy()
# mydict_cpy = dict(mydict)
mydict_cpy["email"] = 'max@xyz.com'
print(mydict_cpy)
print(mydict)


# to merge two dictionaries
mydict = {"name": "Max", "age": 28, "email": "max@xyz.com"}
mydict_2 = dict(name="Mary", age=27, city="Boston")

mydict.update(mydict_2)
print(mydict)



