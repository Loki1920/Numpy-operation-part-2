# numpy operation
import numpy as np
arr = np.arange(15)
print(arr)
#reshape() ,reshapes the given array
arr = arr.reshape(3, 5)
print(arr)
# ravel() create 1-D array
arr = arr.ravel()
print(arr)
print(arr.shape)
# axis in numpy
x = [[1,2,3],[4,5,6],[7,1,0]]
arr = np.array(x)
print("array is :\n",arr)
# sum
print("sum along axis=0:",arr.sum(axis=0))
print("sum along axis=1:",arr.sum(axis=1))
#product
print("product along axis = 0:",arr.prod(axis=0))
print("product along axis = 1:",arr.prod(axis=1))
#Transpose the array
print("transpose  array is :\n",arr.T)
# flat ,return each item 
a = arr.flat
for i in a:
  print(i,end=' ')

#ndim gives dimension 
print("\ndimensions:",arr.ndim)
#size, give number of element
print("size:",arr.size)
#nbytes....gives total bytes consume 
print("total bytes consume:",arr.nbytes)

one = np.array([1,5,9,67,34,98,56])
#argmax - return index of maximum element
print("index of max element:",one.argmax())
#argmin() - index of min element
print("index of min element:",one.argmin())
#argsort - sort as perindex
print("index of sorted element:",one.argsort())



