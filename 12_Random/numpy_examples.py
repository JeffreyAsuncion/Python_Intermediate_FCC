import numpy as np

# numpy has its own random seed
np.random.seed(2)

# produce an array of x elements (floats)
a = np.random.rand(3)
print(a)


# produce an 3x3 array of x elements (floats)
a = np.random.rand(3,3)
print(a)



# produce an array of x elements (integers)
a = np.random.randint(0, 10, 3)
print(a)


# produce an 3x3 array of x elements (integers)
a = np.random.randint(0, 10, (3,3))
print(a)


# a random shuffle 
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)
np.random.shuffle(arr)
print(arr)