import pandas as pd
import numpy as np
a = [1, 7, 2]
# a=np.array([1,7,2])
# a={"x":"test1","y":"test2","z":"test3"}


myvar = pd.Series(a)
# print(myvar)
# print(myvar[0])



# custom lable or custom index
# myvar1 = pd.Series(a, index = ["x", "y", "z"])
# print(myvar1)
# print(myvar1["y"])



# print(myvar["x":"z"])
# print(myvar.index)
# print(myvar.index[2])
# print(myvar.values)
# print(myvar.values[1])


# b=[6,8,10]
# myvar3=pd.Series(b)
# print(myvar.add(myvar3)) #jam
# print(myvar.sub(myvar3)) #menha
# print(myvar.mul(myvar3)) #zarb
# print(myvar.div(myvar3)) #taghsim

myvar4=pd.Series(a,index=[4,5,1])
print(myvar4.loc[1])
print(myvar4.iloc[1])

