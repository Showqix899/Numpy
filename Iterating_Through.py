import numpy as np
#1 D array
ls1 = np.array([1,2,3,4,5,6,7,8,9,10])

#3 D array
ls2=np.array([[[1,2,3],[4,5,6],],[[7,8,9],[10,11,12]]])
print(ls2)

#manualy 
# for x in ls2:
#     for y in x:
#         for z in y:
#             print(z)

#using nditer
for x in np.nditer(ls2):
    print(x)

#it can be also used in 1 D array
for x in np.nditer(ls1):
    print(x)