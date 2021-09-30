import numpy as np

# data type in python

# strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
# integer - used to represent integer numbers. e.g. -1, -2, -3
# float - used to represent real numbers. e.g. 1.2, 42.42
# boolean - used to represent True or False.
# complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j


# data type in numpy

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )


# arr = np.array([1, 2, 3, 4])
# print(arr.dtype)

# arr2 = np.array(['apple', 'banana', 'cherry'])
# print(arr2.dtype)

# arr3 = np.array([1, 2, 3, 4], dtype='S')
# print(arr3)
# print(arr3.dtype)

# # For i, u, f, S and U we can define size as well.

# arr4 = np.array([1, 2, 3, 4], dtype='i4')
# print(arr4)
# print(arr4.dtype)


# Converting Data Type on Existing Arrays
# arr = np.array([1.1, 2.1, 3.1])

# newarr = arr.astype('i')
# print(newarr)
# print(newarr.dtype)

# newarr = arr.astype(int)
# print(newarr)
# print(newarr.dtype)

# arr = np.array([1, 0, 3])
# newarr = arr.astype(bool)
# print(newarr)
# print(newarr.dtype)


# #copy
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# arr[0] = 42
# print(arr)
# print(x)

# #view
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# arr[0] = 42
# print(arr)
# print(x)


# #base
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# y = arr.view()
# print(x.base)
# print(y.base)
# # The copy returns None.
# # The view returns the original array.


# #shape
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(arr)
# print(arr.shape)
# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)
# print('shape of array :', arr.shape)

# #reshape
# #By reshaping we can add or remove dimensions or change number of elements in each dimension.
# #1-D to 2-D
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(4, 3)
# print(newarr)
# 1-D to 3-D
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(2, 3, 2)
# print(newarr)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# print(arr.reshape(2, 4).base)
# Returns Copy or View?The example above returns the original array, so it is a view.

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# newarr = arr.reshape(-1)
# print(newarr)

# itrating
# arr = np.array([1, 2, 3])
# for x in arr:
#   print(x)

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# for x in arr:
#   print(x)

# arr = np.array([1, 2, 3])
# for x in arr:
#   print(x)

# arr = np.array([1, 2, 3])
# for x in arr:
#   print(x)

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# for x in arr:
#   for y in x:
#     for z in y:
#       print(z)

# # nditer
# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# for x in np.nditer(arr):
#   print(x)
# #op_dtypes
# arr = np.array([1, 2, 3])
# for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#   print(x)
  
# #ndenumerate
# arr = np.array([1, 2, 3])
# for idx, x in np.ndenumerate(arr):
#   print(idx, x)

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# for idx, x in np.ndenumerate(arr):
#   print(idx, x)