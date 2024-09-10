import numpy as np

#numpy= Numeric Python
#ndarray= n dimentional array
#numpy is a library for the Python programming language, adding support for large, multi-dimensional arrays and
# matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

np1=np.array([0,1,2,3,4,5,6,7,8,9])


print(np1.shape)

#range method

np2=np.arange(10)
print(np2)

#step
np3=np.arange(0,10,2)
print(np3)

#zeros
np4=np.zeros(10)
print(np4)

#multidimetional zerors

np5=np.zeros((2,10))
print(np5)

#full
np6=np.full((10),6)
print(np6)

#multidimetional full
np7=np.full((2,10),7)
print(np7)

#converting python list to numpy array

mylist=[1,2,3,4,5]
np8=np.array(mylist)
print(np8)

#indexing in numpy array

print(np8[0])
print(np8[3])