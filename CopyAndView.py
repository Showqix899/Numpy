
import numpy as np

#copy method
np1=np.array([1,2,3,4,5,6,7,8,9])
np2=np1.copy()

print(f"original np1{np1}")
print(f'original np2{np2}')

#view method
np3=np.array([1,2,3,4,5,6,7,8,9])
np4=np3.view()

print(f"original np3{np3}")
print(f'original np4{np4}')

np3[0]=69

print(f"changed np3{np3}")
print(f"original np4{np4}")

'''
if we changed the original list 
it will also be changed in the copied list 
if we use view() method to copy
'''