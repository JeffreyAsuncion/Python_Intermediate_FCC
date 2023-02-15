# Secrets modules has three functions
# for passwords, security tokens, or account authentication
# it takes more time than the random module

import secrets

# produce a random integer with exlusion upper bound
a = secrets.randbelow(10)
print(a)


# produce an integer with K random bits
a = secrets.randbits(4)
# range from 0000(0) to 1111(16 exclusive)
print(a)

# secrets choice
mylist = list("ABCDEFGHIJ")
a = secrets.choice(mylist)
print(a)


