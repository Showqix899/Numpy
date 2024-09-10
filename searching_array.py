import numpy as np

ls1=np.array([1,3,4,5,6,7,8,3])

#searching a sinle number
x=np.where(ls1==3)
print(x)
print(x[0])
print(ls1[x[0]])


even=np.where(ls1%2==0)
print(even)
print(even[0])
print(ls1[even[0]])

#searching  multiple number using isin
nums=[3,5,7]
y=np.where(np.isin(ls1,nums))
print(y)
print(y[0])
print(ls1[y[0]])