#statistical summaries
import numpy as np
a = np.array([1,2,3,4,5])
#descriptive statistics(mean, median, mode, variance, std deviation)
print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Mode:", np.bincount(a).argmax())
print("Variance:", np.var(a))
print("Standard Deviation:", np.std(a))

#axis based operations
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Mean along axis 0:", np.mean(b, axis=0))
print("Mean along axis 1:", np.mean(b, axis=1))

