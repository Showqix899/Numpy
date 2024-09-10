
import numpy as np
#1 D
ls1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(ls1)
print(ls1.shape)
#2 D
ls2=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(ls2)
print(ls2.shape)

#converting 1 D to 2 D

ls3=ls1.reshape(3,4) # means 3 row 4 colomn
print(ls3)

ls4=ls1.reshape(2,3,2) #means 2 matrix 3 row 2 colomn
print(ls4)

#back to the  1 D
ls5=ls4.reshape(-1)
print(ls5)