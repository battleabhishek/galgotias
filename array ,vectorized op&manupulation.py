#1d 2d array
import numpy as np

#array creation & manipulation
#create 1d 2d array
a = np.array([1,2,3,4,5])
print(a)
print("shape of a:", a.shape)
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print("shape of b:", b.shape)

#initialised special arrays 
arr3=np.ones((2,3),dtype=int)
print(arr3)
arr4=np.zeros((3,4),dtype=int)
print(arr4)
arr5=np.arange(0,10,2)
print(arr5)
arr6=np.linspace(0,1,5)
print(arr6)
arr7=np.random.rand(3,3)
print(arr7)
arr8=np.random.randint(0,10,(2,3))
print(arr8)

