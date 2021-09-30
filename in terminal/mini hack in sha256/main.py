# import hashlib
import csv

# print ("The available algorithms are : ", end ="")
# print (hashlib.algorithms_guaranteed)

# inputStr = input("enter password : ")
# while int(inputStr) > 10000 or int(inputStr) <= 0:
#     inputStr = input("enter password")

# result = hashlib.sha256(inputStr.encode())
# print("hash is:")
# print(result.hexdigest())

p1 = "4a44dc15364204a80fe80e9039455cc1608281820fe2b24f1e5233ade6af1dd5"
p2 = "a1fb4e703a9ef1fa4936801721ff285a97ac85330856674412e054892afe6972"

# with open('test.csv','w', newline='') as f:
#     for i in range(10000):
#         result = hashlib.sha256(str(i).encode())
#         writer = csv.writer(f)
#         writer.writerows([[f"{result.hexdigest()}",f"{i}"]])
d=dict()
with open('test.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        x = list(row.values())
        h=x[0]
        n=x[1]
        d[h]=n
print(d[p1])
print(d[p32])