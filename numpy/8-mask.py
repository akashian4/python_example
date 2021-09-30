import numpy as np
from numpy.lib.arraysetops import unique

np.random.seed(1)
a = np.random.randint(1, 20, (4, 8))
print(a)

uniqueArray = np.unique(a)
print(uniqueArray)


b = a[a < 13]
print(b)


c = a > 13
print(c)


d = a[c]
print(d)

c1 = a > 18
c2 = a % 3==2

c3=np.logical_and(c1,c2)
c4=np.logical_or(c1,c2)

print(a[c3])
print(a[c4])