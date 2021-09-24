import csv

with open ('height-weight.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
    
file_data.pop(0)
new_Data=[]

for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_Data.append(float(n_num))

n = len(new_Data)
total = 0

for x in new_Data:
    total += x

mean = total/n

print("The average is " + str(mean))