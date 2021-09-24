import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def getMean(data):
    length = len(data)
    total = 0 

    for i in data:
        total += int(i)

    mean = total/length
    return mean

square_list = []

for n in data:
    a = int(n) - getMean(data)
    a = a**2
    square_list.append(a)

sum = 0

for i in square_list:
    sum = sum+i

result = sum/(len(data)-1)

standardDeviation = float(result**0.5)
print(standardDeviation)