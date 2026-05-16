#vactorised oprations
import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])
#elementwise arithmetic operations
print("a + b:", a + b)
print("a - b:", a - b)
print("a * b:", a * b)
print("a / b:", a / b)

#logical filtering (masking)
mask = a > 3
print("Mask (a > 3):", mask)
filtered_a = a[mask]
print("Filtered a (a > 3):", filtered_a)

#bradcasting
c = np.array([1,2,3])
print("a + c:", a + c)


