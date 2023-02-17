org = 5
# no copy just a new variable with the same reference
cpy = org
cpy = 6
print(cpy)
print(org)


# if we deal with lists
# need to be careful
org = [0, 1, 2, 3, 4]
# no copy just a new variable with the same reference
cpy = org
cpy[0] = -10
print(cpy)
print(org)



# to make a copy
# shallow copy  : one level deep, only references of nested child objects
# deep copy     : full independent copy

import copy




# shallow copy
org = [0, 1, 2, 3, 4]

# 3 different ways
# cpy = copy.copy(org)
# cpy = org.copy()
# cpy = list(org)
cpy = org[:]

cpy[0] = -10
print(cpy)
print(org)





# if nested list
org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.deepcopy(org)
cpy[0][1] = -10
print(cpy)
print(org)



# if custom class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee

p1 = Person('Alex', 27)
p2 = copy.copy(p1)

p2.age = 28
print(p2.age)
print(p1.age)

company = Company(p1, p2)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56
print(company_clone.boss.age)
print(company.boss.age)