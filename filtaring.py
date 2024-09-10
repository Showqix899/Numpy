import numpy as np

ls1=np.array([1,2,3,4,5,6,7,8,9])

filtered= ls1 % 2 == 0

print(filtered)

filtered_data=ls1[filtered]
print(filtered_data)