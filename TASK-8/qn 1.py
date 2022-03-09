import numpy as np
numbers = np.array([10,11,12,13,14])
print("REAL :")
print(numbers)
k = 4
new_array = np.zeros(len(numbers) + (len(numbers)-1)*(k))
new_array[::k+1] = numbers
print("\4 0s array:")
print(new_array)