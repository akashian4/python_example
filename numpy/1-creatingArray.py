import numpy as np

# arr = np.array([1, 2, 3, 4, 5])

# print(arr)
# print(type(arr))
# print(np.__version__)

# arr = np.array((1, 2, 3, 4, 5))
# print(arr)


# #0-d array
# arr = np.array(42)
# print(arr)


# #1-d array
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)


# #2-d array
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)


# #3-d array
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(arr)


# #ndim
# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)


# #5-d array
# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)
# print('number of dimensions :', arr.ndim)






#arange
# a=np.arange(2,12,3)
# print(a)


#linspace
# a=np.linspace(0,20,9)
# print(a)


# a=np.linspace(0,20,9,retstep=True)
# print(a)


#ones
# a=np.ones((2,2),dtype=int)
# print(a)


#zeros
# a=np.zeros((2,2))
# print(a)


#random
# a=np.random.random(size=(3,2))
# print(a)

# a=np.random.randint(3,40,(3,2),dtype=int)
# print(a)


#seed (ذخیره ماتریس رندوم)
# np.random.seed(1)
# a=np.random.randint(1,9,(4,3))
# print(a)