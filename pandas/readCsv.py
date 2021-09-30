import pandas as pd

df = pd.read_csv('data.csv')

# print(df) 
# print("-----------------------------") 
# print(df.to_string()) 

# print(df.head()) #print 5 first row
# print(df.head(2)) #print 2 first 
# print(df.tail())  #print 5 last row
# print(df.tail()) 
# print(df.shape) #number of row and column
# print(df.count())
# print(df.values) #convert to list or array
# print(df.describe()) 
#print(df.set_index('Address'))
mysort=df.sort_values('Address',axis=0,inplace=False,ascending=False,na_position='last')
print(mysort)
