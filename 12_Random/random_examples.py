import random

# to make reproducible random set, this is will make a random constitent per run
random.seed(1)

# print a random float from 0 to 1
a = random.random()
print(a)

# print a random number within a range float
a = random.uniform(1, 10)
print(a)

# print a random number within a randint is inclusive
a = random.randint(1, 10)
print(a)

# print a random number within a randrange is exclusive of upper bound
a = random.randint(1, 10)
print(a)

# print a random normalvariate(mu, sigma) 0, 1
# pick a random value from a normal distribution with
# a mean of 0(mu) and the standard deviation of 1(sigma)
a = random.normalvariate(0, 1)
print(a)

# pick a random choice
mylist = list("ABCEFGHIJ")
a = random.choice(mylist)
print(a)

# pick a random sample (no repetition), of size x 
mylist = list("ABCEFGHIJ")
a = random.sample(mylist, 3)
print(a)


# pick a random sample (with repetition), of size k 
mylist = list("ABCEFGHIJ")
a = random.choices(mylist, k=3)
print(a)


# random shuffle in place
mylist = list("ABCEFGHIJ")
random.shuffle(mylist)
print(mylist)


### 3:05:50