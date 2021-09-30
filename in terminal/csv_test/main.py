import csv

testList = []
with open('test.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        testList.append({'name': row[0], 'marks': row[1:]})
print(testList)