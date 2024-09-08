import numpy as np

np1=np.array([1,2,3,4,5,6,7,8,9,10])

#returning 2,3,4,5
print(np1[1:5])

#returning somethin to till the end
#returning 3,to till the end
print(np1[2:])

#returning 2 to 7
print(np1[1:7])

#return negativ slices
#returning 8,9,10
print(np1[-3:])

#returning 3 to 9
print(np1[-8:-1])


#steps
print(np1[0:8]) # 1,2,3,4,5,6,7,8
print(np1[0:8:2]) #1,3,5,7

#print all the item in the array by step 2
print(np1[::2])




# 2 dimetional array slicing

np2=np.array([[1,2,3,4,5],[6,7,8,9,10]])

#pull out single item 

print(np2[1,0]) # 1 2 3 4 5
                # 6 7 8 9 10

print(np2[0:1,2:4]) #3,4

print(np2[1:2,0:3]) #6,7,8

#slice from both row

print(np2[0:3,0:3])

# printing a single element from  2 d array ={8}

print(np2[1,2])