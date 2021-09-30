import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 4, 4])
# x = np.where(arr == 4)
# print(x)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# x = np.where(arr%2 == 1)
# print(x)

#searchsorted --> return index of value
# arr = np.array([6, 7, 8, 9])
# x = np.searchsorted(arr, 7)
# print(x)

# arr = np.array([6, 7, 8, 9])
# x = np.searchsorted(arr, 7, side='right') #index of right side
# print(x)

#Multiple Values
# arr = np.array([1, 3, 5, 7])
# x = np.searchsorted(arr, [2, 4, 6])
# print(x)



# arr = np.array([3, 2, 0, 1])
# print(np.sort(arr))

# arr = np.array(['banana', 'cherry', 'apple'])
# print(np.sort(arr))

# arr = np.array([True, False, True])
# print(np.sort(arr))

# arr = np.array([[3, 2, 4], [5, 0, 1]])
# print(np.sort(arr))


# #filter
# arr = np.array([41, 42, 43, 44])
# x = [True, False, True, False]
# newarr = arr[x]
# print(newarr)


# arr = np.array([41, 42, 43, 44])
# # Create an empty list
# filter_arr = []
# # go through each element in arr
# for element in arr:
#   # if the element is higher than 42, set the value to True, otherwise False:
#   if element > 42:
#     filter_arr.append(True)
#   else:
#     filter_arr.append(False)
# newarr = arr[filter_arr]
# print(filter_arr)
# print(newarr)