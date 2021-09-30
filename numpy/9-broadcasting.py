import numpy as np  


# a = np.array([1,2,3,4,5,6,7])  
# b = np.array([2,4,6,8,10,12,14])  
# c = a*b;  
# print(c)


# a = np.array([1,2,3,4,5,6,7])  
# b = np.array([2,4,6,8,10,12,14,19])  
# c = a*b;  
# print(c)  
################# Error #################

# a = np.array([[1,2,3,4],[2,4,5,6],[10,20,39,3]])  
# b = np.array([2,4,6,8])  
# print("\nprinting array a..")  
# print(a)  
# print("\nprinting array b..")  
# print(b)  
# print("\nAdding arrays a and b ..")  
# c = a + b;  
# print(c)  



a = np.array([[1,2,3],[4,5,6],[7,8,9]])  
  
print("Array:\n",a)  
  
print("\nMedian of array along axis 0:",np.median(a,0))  
print("Mean of array along axis 0:",np.mean(a,0))  
print("Average of array along axis 1:",np.average(a,1))  