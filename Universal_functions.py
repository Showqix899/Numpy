
import numpy as np

#universal function or ufunc()

np1=np.array([1,2,3,4,5,6,7,8,9])
np2=np.array([1,2,3,4,5,6,7,8,9,-10.2,-11.3])


# Square Root for each element

print(np.sqrt(np1))

#absulate value
print(np.absolute(np2))

#exponent value

print(np.exp(np1))

#min/max
print(np.min(np1))
print(np.max(np1))

#negative or positive sign

np3=np.array([-3,-2,-1,0,1,2,3,4,5,6,7,8,9])
print(np3)
print(np.sign(np3))

